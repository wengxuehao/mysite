# _*_coding:utf-8 _*_
# @Time　　:2019/7/19   10:42
# @Author　 : wy
# @ File　　  :urls.py
# @Software  :PyCharm
from django.urls import path

# from apps.books.views import MySearchView
from . import views

app_name = 'books'
urlpatterns = [
    path('search_form/', views.search_form, name='search_form'),
    path('search/', views.search, name='search')
    # path('search/', MySearchView.as_view(), name='haystack_search'),
]
