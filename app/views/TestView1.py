from flask.ext.admin import BaseView, expose
from app import admin
class TestView1(BaseView):
    @expose('/')
    def index(self):
        return self.render('index/testview1.html')

#admin.add_view(TestView1(name='Test1'))