import datetime

from django.db import models

# Create your models here.
from django.utils import timezone


class Man_Model(models.Model):
    name = models.CharField(max_length=20, verbose_name='name')
    age = models.IntegerField(default=10, verbose_name='age')

    class Meta:
        verbose_name = "man"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Plant_Model(models.Model):
    name = models.CharField(max_length=20, verbose_name='p_name')
    age = models.IntegerField(default=10, verbose_name='p_age')
    owner = models.ForeignKey(Man_Model, on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name = "plant"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    atomic = False

    class Meta:
        # 自定义表名称
        db_table = 'Q_table'
        verbose_name = 'question'

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    # ForeignKey, ManyToManyField and OneToOneField 接收的第一个参数为模型的类名，
    # 后面可以添加一个 verbose_name 参数：
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    # choices
    # 每个二元组的第一个值会储存在数据库中，而第二个值将只会用于显示作用。
    # 对于一个模型实例，要获取该字段二元组中相对应的第二个值，使用 get_FOO_display() 方法。例如：
    # get_shirt_size_display()
    # TODO 该参数接收一个可迭代的列表或元组（基本单位为二元组）。如果指定了该参数，在实例化该模型时，该字段只能取选项列表中的值。
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default='')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()



