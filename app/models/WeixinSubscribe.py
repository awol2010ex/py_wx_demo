from app import db
#欢迎语
class WeixinSubscribe(db.Model):
    __tablename__ = 'weixin_subscribe'
    id = db.Column(db.String(36),primary_key = True)
    accountid= db.Column(db.String(255) ,db.ForeignKey('weixin_account.id') )
    addtime= db.Column(db.String(255))
    msgtype= db.Column(db.String(255))
    templateid= db.Column(db.String(255),db.ForeignKey('weixin_texttemplate.id'))
    templatename= db.Column(db.String(255))
    weixinaccount = db.relationship('WeixinAccount', backref='weixin_subscribe')
    weixintexttemplate = db.relationship('WeixinTexttemplate', backref='weixin_subscribe')
    def __str__(self):
        return self.templateName