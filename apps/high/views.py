import csv

from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django_redis import get_redis_connection

# 获取redis数据库连接
redis_conn = get_redis_connection('default')
# Create your views here.kaskakakak

import datetime

from django.template import loader, Context, RequestContext, TemplateDoesNotExist
from reportlab.pdfgen import canvas


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


def about_pages(request):
    try:
        return render(request, 'about_page.html')
    except TemplateDoesNotExist:
        raise Http404()


def my_image(request):
    image_data = open('static/images/307128.png', "rb").read()
    # 返回图片格式并直接展示，前端模板设置接收，后端返回需要设置content_type
    return HttpResponse(image_data, content_type="image/png")


UNRULY_PASSENGERS = [146, 184, 235, 200, 226, 251, 299, 273, 281, 304, 203]


def unruly_passengers_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    # response['Content‐Disposition'] = 'attachment; filename=unruly.csv'
    response['Content-Disposition'] = 'attachment; filename="下载.csv"'
    # Create the CSV writer using the HttpResponse as the "file."
    writer = csv.writer(response)
    writer.writerow(['Year', 'Unruly Airline Passengers'])
    for (year, num) in zip(range(1995, 2006), UNRULY_PASSENGERS):
        writer.writerow([year, num])
    return response


def hello_pdf(request):
    name = redis_conn.get('name')
    print(name)
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    # response['Content‐Disposition'] = 'attachment; filename="hello.pdf"'
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response


def register(request):
    print(request.META.keys())
    redis_conn.setex('name', 100000, "this is name")
    # 使用django自带的注册模块
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
        # 注册成功后跳转到首页
        return HttpResponseRedirect("index")
    else:
        form = UserCreationForm()
        return render_to_response("registration/register.html", {
            'form': form,
        })


def index(request):
    return HttpResponse('这是注册成功后的主页')
