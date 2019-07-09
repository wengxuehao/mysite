# Create your tests here.

import datetime

from django.test import TestCase
from django.utils import timezone

# from models import Question
# from django_polls.polls import Question
# TODO 当写测试文件时候,导入路径一定要写成绝对路径
from apps.polls.models import Question

'''
python manage.py test polls
运行测试代码将会寻找 polls 应用里的测试代码
它找到了 django.test.TestCase 的一个子类
它创建一个特殊的数据库供测试使用
它在类中寻找测试方法——以 test 开头的方法。
在 test_was_published_recently_with_future_question 方法中，它创建了一个 pub_date 值为 30 天后的 Question 实例。
接着使用 assertls() 方法，发现 was_published_recently() 返回了 True，而我们期望它返回 False。
'''


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        过去
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        最近
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        将来
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
