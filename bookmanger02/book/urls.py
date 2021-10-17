# -*— codeing = utf-8 -*—
# @Time : 2021/10/1812:50 上午
# @Author : 房淡淡
# @File : urls.py
# @Software : PyCharm
from django.urls import path
from book.views import index
urlpatterns = [
    path('index/',index),
]
