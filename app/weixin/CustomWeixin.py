try:
    from flask import current_app, request, Response
except ImportError:
    current_app = None
    request = None
    Response = None
import time
import hashlib
from datetime import datetime
from app.models.WeixinAccount import  WeixinAccount
from app.models.WeixinAutoresponse import  WeixinAutoresponse
from app.models.WeixinReceivetext import WeixinReceivetext
from app.models.WeixinSubscribe import  WeixinSubscribe
from app.models.WeixinPlugins import WeixinPlugins
from flask_weixin import Weixin
from app import app
from app import db
import uuid

from app.weixin.plugins  import plugins

class CustomWeixin(Weixin):
    def view_func(self,appuuid):
        """Default view function for Flask app.

        This is a simple implementation for view func, you can add it to
        your Flask app::

            weixin = Weixin(app)
            app.add_url_rule('/', view_func=weixin.view_func)
        """
        
        token =WeixinAccount.query.filter_by(id=appuuid).first().accounttoken
        

        if request is None:
            raise RuntimeError('view_func need Flask be installed')

        signature = request.args.get('signature')
        timestamp = request.args.get('timestamp')
        nonce = request.args.get('nonce')
        if not self.validate(signature, timestamp, nonce ,token):
            return 'signature failed', 400

        if request.method == 'GET':
            echostr = request.args.get('echostr', '')
            return echostr

        try:
            ret = self.parse(request.data)
        except ValueError:
            return 'invalid', 400

        ret['appuuid'] =appuuid
        if 'type' not in ret:
            # not a valid message
            return 'invalid', 400

        if ret['type'] == 'text' and ret['content'] in self._registry:
            func = self._registry[ret['content']]
        else:
            ret_set = frozenset(ret.items())
            matched_rules = (
                _func for _func, _limitation in self._registry_without_key
                if _limitation.issubset(ret_set))
            func = next(matched_rules, None)  # first matched rule

        if func is None:
            if '*' in self._registry:
                func = self._registry['*']
            else:
                func = 'failed'

        if callable(func):
            text = func(**ret)
        else:
            # plain text
            text = self.reply(
                username=ret['sender'],
                sender=ret['receiver'],
                content=func,
            )
        print("Text==")
        print(text)
        return Response(text, content_type='text/xml; charset=utf-8')
    def validate(self, signature, timestamp, nonce ,token):
        """Validate request signature.

        :param signature: A string signature parameter sent by weixin.
        :param timestamp: A int timestamp parameter sent by weixin.
        :param nonce: A int nonce parameter sent by weixin.
        """
        
        if not token:
            raise RuntimeError('WEIXIN_TOKEN is missing')

        if self.expires_in:
            try:
                timestamp = int(timestamp)
            except (ValueError, TypeError):
                # fake timestamp
                return False

            delta = time.time() - timestamp
            if delta < 0:
                # this is a fake timestamp
                return False

            if delta > self.expires_in:
                # expired timestamp
                return False

        values = [token, str(timestamp), str(nonce)]
        s = ''.join(sorted(values))
        hsh = hashlib.sha1(s.encode('utf-8')).hexdigest()
        return signature == hsh
    view_func.methods = ['GET', 'POST']
weixin = CustomWeixin(app)
app.add_url_rule('/wx/<string:appuuid>', view_func=weixin.view_func)


'''
jing_music = (
    'http://cc.cdn.jing.fm/201310171130/19e715ce8223efd159559c15de175ab6/'
    '2012/0428/11/AT/2012042811ATk.m4a'
)
'''
#自动回复
@weixin('*')
def reply_all(**kwargs):
    username = kwargs.get('sender')
    sender = kwargs.get('receiver')
    message_type = kwargs.get('type')
    content = kwargs.get('content', message_type)
    appuuid = kwargs.get('appuuid')
    #消息日志记录 start
    ReceiveObject =WeixinReceivetext()
    ReceiveObject.id =str(uuid.uuid1()).replace('-','')
    ReceiveObject.content =content
    ReceiveObject.createtime =datetime.now()
    ReceiveObject.fromusername =username
    ReceiveObject.tousername =sender
    ReceiveObject.accountid =sender
    ReceiveObject.msgtype=message_type
    ReceiveObject.msgid =kwargs.get('id')
    db.session.add(ReceiveObject)
    db.session.commit()
    #消息日志记录 end

    #自动回复记录
    replycontent =content
    res=WeixinAutoresponse.query.filter_by(accountid=appuuid ,keyword=content).first()
    if res:
        replycontent=res.weixintexttemplate.content
    else:
        plugin=WeixinPlugins.query.filter(" '"+content+"'  like '%'||keyword||'%' and  accountid='"+appuuid+"' ").first()
        if plugin:
            #搜索插件
            if plugin.pluginfile in plugins.keys():
                p=plugins[plugin.pluginfile]
                if p.check(message_type, content,appuuid): #检测匹配
                    replycontent=p.reply(message_type, content,appuuid)
    print(replycontent)
    r=weixin.reply(
            username, sender=sender, content=replycontent
    )
    print(r)
    return r
'''
    if content == 'music':
        return weixin.reply(
            username, type='music', sender=sender,
            title='Weixin Music',
            description='weixin description',
            music_url=jing_music,
            hq_music_url=jing_music,
        )
    elif content == 'news':
        return weixin.reply(
            username, type='news', sender=sender,
            articles=[
                {
                    'title': 'Weixin News',
                    'description': 'weixin description',
                    'picurl': '',
                    'url': 'http://lepture.com/',
                }
            ]
        )
    else:
        return weixin.reply(
            username, sender=sender, content=content
        )

'''
#关注
@weixin.register(type='event', event='subscribe')
def send_welcome(**kwargs):
    username = kwargs.get('sender')
    sender = kwargs.get('receiver')
    appuuid = kwargs.get('appuuid')
    content ='Thanks for follow!'
    s=WeixinSubscribe.query.filter_by(accountid=appuuid).first()
    if s: 
        content =s.weixintexttemplate.content
    return weixin.reply(username, sender=sender, content=content)
#取消关注
@weixin.register(type='event', event='unsubscribe')
def send_welcome(**kwargs):
    username = kwargs.get('sender')
    sender = kwargs.get('receiver')
    return weixin.reply(username, sender=sender, content='Thanks for not follow!')