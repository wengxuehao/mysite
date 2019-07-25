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
    first_name = models.CharField(max_length=30, verbose_name='姓氏')
    last_name = models.CharField(max_length=40, verbose_name='名字')
    email = models.EmailField(verbose_name='郵箱')

    class Meta:
        db_table = 'Author_table'
        verbose_name = 'author'

    def __str__(self):
        return self.first_name


class BookManager(models.Manager):
    # 我们建立了一个BookManager类，它继承了django.db.models.Manager。这个类只有一个
    # title_count()方法，用来做统计。
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pages = models.IntegerField(verbose_name='页数', default=300)
    # publication_date = models.DateField()
    objects = BookManager()

    class Meta:
        db_table = 'Book_table'
        verbose_name = 'book'

    def __str__(self):
        return self.title
