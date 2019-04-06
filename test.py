from django.shortcuts import reverse, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from ormtest import view


def test(request):
    return render_to_response('test.html')


def profile(request):
    if request.GET.get('username'):
        return HttpResponse('%s,欢迎来到个人中心！')
    else:

        return redirect(reverse(view.hello))
