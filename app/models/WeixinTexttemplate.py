from app import db
class WeixinTexttemplate(db.Model):
    __tablename__ = 'weixin_texttemplate'
    id = db.Column(db.String(32),primary_key = True)
    addtime= db.Column(db.String(255))
    content= db.Column(db.String(255))
    templatename= db.Column(db.String(255))
    accountid= db.Column(db.String(100),db.ForeignKey('weixin_account.id') )
    weixinaccount = db.relationship('WeixinAccount', backref='weixin_texttemplate')
    def __str__(self):
        return self.templatename