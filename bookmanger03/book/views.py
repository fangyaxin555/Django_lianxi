from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from book.models import BookInfo
# Create your views here.
def index(request):
    return HttpResponse('ok')

def create(request):
    book = BookInfo.objects.create(
        name='三毛流浪记',
        pub_date='2002-1-1',
        readcount=1000,
    )
    return HttpResponse('ok')

def shop(request,city,shop):
    # str = f'你好{city} 你好{shop}'
    # print(str)

    #获取查询字符串的值
    query_param = request.GET
    print(query_param.get('order'))
    print(query_param.getlist('order'))
    return HttpResponse('你好%s %s'%(city,shop))

def register(request):
    data = request.POST
    print(data)
    return HttpResponse('ok')

def json(request):
    body = request.body
    body = body.decode('utf-8')
    print(body)
    import json
    body = json.loads(body)
    print(body)
    ########使用请求头############
    head = request.META
    print(head.get('port'))

    return HttpResponse('ok')

#第一次访问的时候设置cookie
def set_cookie(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    response = HttpResponse('set_cookie')
    response.set_cookie('name',username,max_age=60*60*60)
    response.set_cookie('mima',password)
    return response
#第二次以上访问的时候，就返回获取浏览器给的cookie
def get_cookie(request):
    cookie = request.COOKIES
    return JsonResponse(data=cookie)


########################session的相关知识
def set_session(request):
    #获得用户的信息
    user_name = request.GET.get('username')
    #设置session
    user_id = 1
    request.session['username'] = user_name
    request.session['userid'] = user_id

    return HttpResponse("set_session")

def get_session(request):
    username = request.session.get('username')
    userid = request.session.get('userid')
    return HttpResponse(f'用户名字\t{username}\r\n用户id\t{userid}')


########################视图类的相关知识
from django.views import View
class LoginView(View):
    def get(self,request):
        return HttpResponse('getget')
    def post(self,request):
        return HttpResponse('post,post')


from django.contrib.auth.mixins import LoginRequiredMixin
class OrderView(LoginRequiredMixin,View):

    def get(self,request):
        return HttpResponse('getget')

    def post(self,request):
        return HttpResponse('post,post')







