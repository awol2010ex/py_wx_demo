from app import db

#插件表
class WeixinPlugins(db.Model):
    __tablename__ = 'weixin_plugins'
    id = db.Column(db.String(32),primary_key = True)
    pluginname= db.Column(db.String(200))
    accountid= db.Column(db.String(32),db.ForeignKey('weixin_account.id') )
    pluginfile= db.Column(db.String(200))
    keyword= db.Column(db.String(200))
    weixinaccount = db.relationship('WeixinAccount', backref='weixin_plugins')

    def __str__(self):
        return self.pluginname