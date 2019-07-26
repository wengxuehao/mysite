# _*_coding:utf-8 _*_
# @Time　　:2019/7/24   14:39
# @Author　 : wy
# @ File　　  :urls.py
# @Software  :PyCharm
from django.urls import path

from apps.high import views

appname = 'high'
urlpatterns = [
    path('about', views.about_pages),
    path('image', views.my_image),
    path('csv', views.unruly_passengers_csv),
    path('pdf', views.hello_pdf),
    path('zhuce',views.register),
    path('index',views.index)

]
