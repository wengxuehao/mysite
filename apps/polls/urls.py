#  _*_ coding:UTF-8 _*_
from django.urls import path
from rest_framework import routers

from . import views

'''教程项目只有一个应用，polls 。
在一个真实的 Django 项目中，可能会有五个，十个，二十个，甚至更多应用。
Django 如何分辨重名的 URL 呢？举个例子，polls 应用有 detail 视图，可能另一个博客应用也有同名的视图。
Django 如何知道 {% url %} 标签到底对应哪一个应用的 URL 呢'''
# 为URL名称添加上命名空间
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('get_man/',views.ManListView.as_view(),name='man_list'),
    path('get_man/', views.ManView.as_view(), name='get_man')

]
