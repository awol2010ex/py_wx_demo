


from app import db
#微信账号表
class WeixinAccount(db.Model):
    __tablename__ = 'weixin_account'
    id = db.Column(db.String(36),primary_key = True)
    accountname= db.Column(db.String(200)) #账号名
    accounttoken= db.Column(db.String(200)) #token
    accounttype= db.Column(db.String(50)) #账号类型 1 服务号 2 订阅号
    accountemail= db.Column(db.String(200)) #账号邮箱
    accountdesc= db.Column(db.String(500)) #账号描述
    accountappid= db.Column(db.String(200)) #账号APPID
    accountappsecret= db.Column(db.String(500)) #账号 appsecret
    def __str__(self):
        return self.accountname