from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
class Row1(MiddlewareMixin):
    def process_request(self,request):
        print('1')

    def process_view(self,request,view_func,view_func_args,view_func_kwargs):
        print('①')

    def process_response(self,request,response):
        print('一')
        return response

class Row2(MiddlewareMixin):
    def process_request(self,request):
        print('2')
        # if request.method=='GET':
        #     return HttpResponse('100')
    def process_view(self,request,view_func,view_func_args,view_func_kwargs):
        print('②')

    def process_response(self,request,response):
        print('二')
        return response

class Row3(MiddlewareMixin):
    def process_request(self,request):
        print(3)
    def process_view(self,request,view_func,view_func_args,view_func_kwargs):
        print('③')

    def process_response(self,request,response):
        print('三')
        return response

from django.middleware.cache import FetchFromCacheMiddleware