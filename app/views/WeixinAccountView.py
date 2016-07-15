from flask_admin.contrib.sqla import ModelView
from app import db,admin
from app.models.WeixinAccount import  WeixinAccount
#微信账号维护页面
class WeixinAccountView(ModelView):
    can_delete = False
    can_create = False
    page_size =10
    form_args ={
        'accountname':{'label':'账号'}
    }
    form_choices={
        'accounttype':[ 
           ('1','服务号'),
           ('2','订阅号')
        ]
    }
    column_choices={
        'accounttype':[ 
           ('1','服务号'),
           ('2','订阅号')
        ]
    }
    column_labels=dict(
        accountname='账号',accounttoken='Token',accounttype='账号类型',
        accountemail='账号邮箱',accountdesc='账号描述',accountappid='账号APPID',
        accountappsecret='appsecret'
    )

admin.add_view(WeixinAccountView(WeixinAccount,db.session,name='微信账号'))

