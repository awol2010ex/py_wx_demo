from flask_admin.contrib.sqla import ModelView
from app import db,admin
from app.models.WeixinAutoresponse import  WeixinAutoresponse
from app.models.WeixinAccount import  WeixinAccount
from app.models.WeixinSubscribe import  WeixinSubscribe
#欢迎语页面
class WeixinSubscribeView(ModelView):
    column_labels={ 'addtime':'添加时间'  ,'msgtype':'消息类型' ,'templatename':'模板名称','weixinaccount':'微信账号','weixintexttemplate':"模板" ,
    'accountname':'微信账号','weixintexttemplate.templatename':"模板",'weixinaccount.accountname':'微信账号' }
    column_list=('weixinaccount','weixintexttemplate', 'addtime','msgtype')
    
    page_size =10
admin.add_view(WeixinSubscribeView(WeixinSubscribe,db.session,name='欢迎语'))