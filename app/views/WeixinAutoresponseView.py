from flask_admin.contrib.sqla import ModelView
from app import db,admin
from app.models.WeixinAutoresponse import  WeixinAutoresponse
from app.models.WeixinAccount import  WeixinAccount
#微信自动回复模板页面
class WeixinAutoresponseView(ModelView):
    
    column_labels={ 'addtime':'添加时间' ,'keyword':'关键字' ,'msgtype':'消息类型' ,'templatename':'模板名称','weixinaccount':'微信账号','weixintexttemplate':"模板" ,
    'accountname':'微信账号','weixintexttemplate.templatename':"模板",'weixinaccount.accountname':'微信账号' }
    column_list=('weixinaccount.accountname','weixintexttemplate.templatename', 'addtime', 'keyword', 'templatename','msgtype')
    
    page_size =10
admin.add_view(WeixinAutoresponseView(WeixinAutoresponse,db.session,name='自动回复'))