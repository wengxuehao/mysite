from django.contrib import admin

# Register your models here.
from .models import Man_Model, Plant_Model, Choice, Person
from .models import Question


class Man_Admin(admin.ModelAdmin):
    list_display = ['name', 'age']


admin.site.register(Man_Model, Man_Admin)


class Plant_Admin(admin.ModelAdmin):
    list_display = ['name', 'age', 'owner']


admin.site.register(Plant_Model, Plant_Admin)


class ChoiceInline(admin.TabularInline):
    # TODO StackedInline/TabularInline(关联对象用表格式展示)
    # “Choice
    # 对象要在
    # Question
    # 后台页面编辑。默认提供
    # 3个足够的选项字段。”
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    '''为表单选择一个直观的排序方法就显得你的针很细了。
说到拥有数十个字段的表单，你可能更期望将表单分为几个字段集：'''
    # TODO fieldsets 元组中的第一个元素是字段集的标题
    # TODO Django 知道要将 ForeignKey 在后台中以选择框 <select> 的形式展示。此时，我们只有一个投票。
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # 显示列名
    list_filter = ['pub_date']  # 右侧筛选
    search_fields = ['question_text']  # 在列表的顶部增加一个搜索框
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)


class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


admin.site.register(Person, PersonAdmin)
