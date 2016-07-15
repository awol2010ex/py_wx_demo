from app import db
#自动回复表
class WeixinAutoresponse(db.Model):
    __tablename__ = 'weixin_autoresponse'
    id = db.Column(db.String(32),primary_key = True)

    addtime= db.Column(db.String(255))
    keyword= db.Column(db.String(255))
    msgtype= db.Column(db.String(255))
    rescontent= db.Column(db.String(255),db.ForeignKey('weixin_texttemplate.id') )
    templatename= db.Column(db.String(255))
    accountid= db.Column(db.String(100),db.ForeignKey('weixin_account.id')  )
    weixinaccount = db.relationship('WeixinAccount', backref='weixin_autoresponse')
    weixintexttemplate = db.relationship('WeixinTexttemplate', backref='weixin_autoresponse')
    def __str__(self):
        return self.keyword