# -*— codeing = utf-8 -*—
# @Time : 2021/10/2012:41 上午
# @Author : 房淡淡
# @File : urls.py
# @Software : PyCharm
from django.urls import path
from person.views import index
urlpatterns = [
    path('index/', index),
]