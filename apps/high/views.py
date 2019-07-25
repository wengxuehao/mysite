from django.shortcuts import render

# Create your views here.

import datetime

from django.template import loader, Context, RequestContext


def day_archive(request, year, month, day):
    # The following statement raises a TypeError!
    date = datetime.date(year, month, day)


def custom_proc(request):
    # A context processor that provides 'app', 'user' and 'ip_address'
    # 我们定义一个函数 custom_proc 。这是一个context处理器，它接收一个 HttpRequest 对象，然后
    # 返回一个字典，这个字典中包含了可以在模板context中使用的变量。
    return {
        'app': 'My app',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR']
    }


def view_1(request):
    # ...
    t = loader.get_template('template1.html')
    c = RequestContext(request, {'message': 'I am view 1.'},
                       processors=[custom_proc])
    return t.render(c)


def view_2(request):
    # ...
    t = loader.get_template('template2.html')
    c = RequestContext(request, {'message': 'I am the second view.'}, processors=[custom_proc])
    return t.render(c)
