from django.contrib import admin

# Register your models here.
from apps.books.models import Publisher, Author, Book


class PublisherAdmin(admin.ModelAdmin):
    list_filter = ['name']  # 右侧筛选
    list_display = ['name', 'address']


admin.site.register(Publisher, PublisherAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_filter = ['first_name']  # 右侧筛选--过滤器
    search_fields = ['first_name']  # 在列表的顶部增加一个搜索框
    list_display = ['first_name', 'last_name', 'email']


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', "publisher"]
    fields = ('title', 'authors', 'publisher')


admin.site.register(Book, BookAdmin)
