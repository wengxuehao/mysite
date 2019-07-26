# _*_coding:utf-8 _*_
# @Time　　:2019/7/25   14:44
# @Author　 : wy
# @ File　　  :demo_senmail.py
# @Software  :PyCharm
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.utils import parseaddr, formataddr
import smtplib

from_addr = 'wengxh_09@163.com'  # 用来发送邮件的邮箱地址
password = 'wxh19950905'  # 邮箱密码或者是授权密码
to_addr = ['1041668005@qq.com']  # 目标邮箱地址
smtp_server = 'smtp.163.com'  # 这里是新浪的SMTP服务器地址
# 发送的信息格式
content = MIMEText('hello,send by Python', 'plain', 'utf-8')
msg = MIMEMultipart()
msg['From'] = Header(from_addr)  # 定义发件人
msg['Subject'] = Header('Python 邮件测试', 'utf-8')  # 定义邮件名
msg.attach(content)  # 加上邮件的内容
try:
    server = smtplib.SMTP()
    server.connect(smtp_server, 25)  # 连接SMTP服务器
    server.set_debuglevel(1)  # 打印调试信息
    server.login(from_addr, password)  # 登陆邮箱
    server.sendmail(from_addr, to_addr, msg.as_string())  # 发送邮件
    print("Send successfully!")
except smtplib.SMTPException as e:
    server.quit()  # 退出
    print("发送失败")
