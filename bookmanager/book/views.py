from django.shortcuts import render

# Create your views here.
"""
视图函数有两个要求：
    1.视图函数的第一个参数就是接受请求
    2.视图函数必须返回一个响应 httpresponse
"""
from django.http import HttpResponse
def index(request):
    #render 函数为渲染模版的函数 实际返回的也是httpsponse

    #模拟从数据库查找的函数
    context = {'name':'马上双11，点击有惊喜'}
    return render(request,'book/index.html',context=context)