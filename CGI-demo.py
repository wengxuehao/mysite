# _*_coding:utf-8 _*_
# @Time　　:2019/7/15   15:56
# @Author　 : wy
# @ File　　  :CGI-demo.py
# @Software  :PyCharm
# !/usr/bin/env python
import MySQLdb

print("Content‐Type: text/html\n")
print("<html><head><title>Books</title></head>")
print("<body>")
print("<h1>Books</h1>")
print("<ul>")
connection = MySQLdb.connect(user='wengxh', passwd='mysql', db='shiwu')
cursor = connection.cursor()
cursor.execute("SELECT username FROM user ")
for row in cursor.fetchall():
    print("<li>%s</li>" % row[0])
print("</ul>")
print("</body></html>")
