# -*— codeing = utf-8 -*—
# @Time : 2021/10/2012:41 上午
# @Author : 房淡淡
# @File : urls.py
# @Software : PyCharm
from django.urls import path,converters
from django.urls.converters import register_converter
from book.views import index,create,shop,register,json,set_cookie,get_cookie,set_session,get_session
from book.views import LoginView,OrderView
#1.重写转换器
class mobileConverter:
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value
#注册转换器
register_converter(mobileConverter,"mobile")

urlpatterns = [
    path('index/', index),
    path('create/',create),
    path('register/', register),
    path('json/',json),
    #使用转换器，系统自带的和重写的
    path('<int:city>/<mobile:shop>/',shop),
    path('set_cookie/',set_cookie),
    path('get_cookie/',get_cookie),
    path('set_session/',set_session),
    path('get_session/',get_session),
    path('login/',LoginView.as_view()),
    path('order/',OrderView.as_view()),
]