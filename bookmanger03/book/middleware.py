# -*— codeing = utf-8 -*—
# @Time : 2021/10/215:00 下午
# @Author : 房淡淡
# @File : middleware.py
# @Software : PyCharm
from django.utils.deprecation import MiddlewareMixin

class TestMiddleWare(MiddlewareMixin):

    def process_request(self,request):
        print('midlleware_request')
        username = request.COOKIES.get('name')
        if username is None:
            print("don't have")
        else:
            print('have')
    def process_response(self,request,response):
        print('middleware_reponse')
        return response