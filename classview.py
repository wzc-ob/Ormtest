from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views import View
def abc(request):
    return render_to_response('detail.html')

class BookDetailView(View):
    def post(self, request, *args, **kwargs):
        return HttpResponse("书籍添加成功！")

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("您当前采用的method是：%s，本视图只支持使用post请求！" % request.method)