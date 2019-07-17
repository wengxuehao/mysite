from django.contrib import admin

# Register your models here.
from apps.books.models import Publisher, Author, Book


class Publisher_Admin(admin.ModelAdmin):
    list_filter = ['name']  # 右侧筛选
    list_display = ['name', 'address']


admin.site.register(Publisher, Publisher_Admin)


class Author_Admin(admin.ModelAdmin):
    list_filter = ['first_name']  # 右侧筛选--过滤器
    search_fields = ['first_name']  # 在列表的顶部增加一个搜索框
    list_display = ['first_name', 'last_name', 'email']



admin.site.register(Author, Author_Admin)


class Book_Admin(admin.ModelAdmin):
    list_display = ['title', "publisher", 'publication_date']
    fields = ('title', 'authors', 'publisher', 'publication_date')


admin.site.register(Book, Book_Admin)
