# _*_coding:utf-8 _*_
# @Time　　:2019/7/19   15:00
# @Author　 : wy
# @ File　　  :search_indexes.py
# @Software  :PyCharm
from haystack import indexes
# 引入你项目下的model（也就是你要将其作为检索关键词的models）
from .models import Book


# model名 + Index作为类名
class BookIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # 对书名，书作者搜索
    title = indexes.CharField(model_attr='title')
    # authors = indexes.CharField(model_attr='authors')
    # lyric = indexes.CharField(model_attr='lyric')

    def get_model(self):
        return Book

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
