from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        # 自定义表名称
        db_table = 'Publisher_table'
        verbose_name = 'publisher'

    def __str__(self):
        return self.name


class Author(models.Model):
    # verbose_name 用作显示在后台的列名称
    first_name = models.CharField(max_length=30,verbose_name='姓氏')
    last_name = models.CharField(max_length=40,verbose_name='名字')
    email = models.EmailField(verbose_name='郵箱')

    class Meta:
        db_table = 'Author_table'
        verbose_name = 'author'


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    publication_date = models.DateField()

    class Meta:
        db_table = 'Book_table'
        verbose_name = 'book'
