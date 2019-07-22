# _*_coding:utf-8 _*_
# @Time　　:2019/7/22   16:13
# @Author　 : wy
# @ File　　  :demo.py
# @Software  :PyCharm
from django.http import HttpResponse
from django_redis import get_redis_connection

def getname():
    conn = get_redis_connection('django')
    name = conn.get('name').decode('utf-8')
    return name


print(getname())