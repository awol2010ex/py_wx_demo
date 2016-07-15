from flask import Flask
from flask.ext.admin import Admin, BaseView, expose
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
#config
app.config.from_object('config')
#database
db = SQLAlchemy(app)


#flask admin
admin = Admin(app, name='weixin platform', template_mode='bootstrap3')
# Add administrative views here



from app.views import *
from app.weixin import CustomWeixin






