from flask_admin.contrib.sqla import ModelView
from app import db,admin
from app.models.WeixinReceivetext import  WeixinReceivetext
#微信消息日志列表页面
class WeixinReceivetextView(ModelView):
    can_delete= False
    can_create=False
    can_edit =False
    page_size =10
admin.add_view(WeixinReceivetextView(WeixinReceivetext,db.session,name='消息日志'))