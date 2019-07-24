from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views import View
from django_redis import get_redis_connection
# 使用redis配置，缓存数据，并设置过期时间

from apps.books.models import Book, Publisher, Author
# from haystack.generic_views import SearchView


def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        conn = get_redis_connection('default')
        name = conn.set('name', 'zhangsan', 10000)
        print(name)
        print(request.user)
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_results.html',
                                  {'books': books, 'query': q})
    else:
        return render_to_response('search_form.html', {'error': True})
