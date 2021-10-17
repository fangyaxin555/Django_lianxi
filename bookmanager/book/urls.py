# -*— codeing = utf-8 -*—
# @Time : 2021/10/172:01 下午
# @Author : 房淡淡
# @File : urls.py.py
# @Software : PyCharm
from django.urls import path
from book.views import index
urlpatterns = [
    path('index/', index)
]