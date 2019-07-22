from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views import View
from django_redis import get_redis_connection

from apps.books.models import Book, Publisher, Author
# from haystack.generic_views import SearchView


def search_form(request):
    conn = get_redis_connection('django')

    name = conn.set('name','zhangsan',10000).decode('utf-8')
    print(name)
    return render_to_response('search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_results.html',
                                  {'books': books, 'query': q})
    else:
        return render_to_response('search_form.html', {'error': True})
