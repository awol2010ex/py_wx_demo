from flask_admin.contrib.sqla import ModelView
from app import db,admin
from app.models.WeixinPlugins import  WeixinPlugins
from app.models.WeixinAccount import  WeixinAccount
import uuid
#插件维护页面
class WeixinPluginsView(ModelView):
    page_size =10
    def on_model_change(self, form, weixinplugins, is_created):
        weixinplugins.id =str(uuid.uuid1()).replace('-','')
admin.add_view(WeixinPluginsView(WeixinPlugins,db.session,name='插件'))