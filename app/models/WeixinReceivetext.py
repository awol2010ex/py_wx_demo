from app import db
#接收信息日志表
class WeixinReceivetext(db.Model):
    __tablename__ = 'weixin_receivetext'
    id = db.Column(db.String(32),primary_key = True)
    content= db.Column(db.String(255)) #内容
    createtime= db.Column(db.DateTime)
    fromusername= db.Column(db.String(255))
    msgid= db.Column(db.String(255))
    msgtype= db.Column(db.String(255))
    rescontent= db.Column(db.String(255))
    response= db.Column(db.String(255))
    tousername= db.Column(db.String(255))
    accountid= db.Column(db.String(100))
    nickname= db.Column(db.String(200))