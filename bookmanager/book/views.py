from django.shortcuts import render

# Create your views here.
"""
视图函数有两个要求：
    1.视图函数的第一个参数就是接受请求
    2.视图函数必须返回一个响应 httpresponse
"""
from django.http import HttpResponse
def index(request):
    return HttpResponse("ok")