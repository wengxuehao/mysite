"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.db import router
# from django.db import router
from django.urls import path, include
from rest_framework import routers

from apps.polls import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
# router.register(r'polls', views.ManView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('apps.polls.urls')),
    path('books/', include('apps.books.urls')),
    path('high/',include('apps.high.urls')),
    # path('', ''),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path(r'search/', include('haystack.urls')),
]
