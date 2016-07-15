from flask_admin.contrib.sqla import ModelView
from app import db,admin
from app.models.WeixinTexttemplate import  WeixinTexttemplate
class WeixinTexttemplateView(ModelView):
    
    column_labels={ 'addtime':'添加时间' ,'templatename':'模板名称','weixinaccount':'微信账号',
    'accountname':'微信账号','content':'内容','weixin_autoresponse':'自动回复' }
    page_size =10
admin.add_view(WeixinTexttemplateView(WeixinTexttemplate,db.session,name='消息模板'))