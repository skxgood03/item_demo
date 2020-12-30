from haystack import indexes
from post.models import *

class PostIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)   #使用模板

    # 给title和content设置索引
    title =indexes.NgramField(model_attr='title')
    content =indexes.NgramField(model_attr='content')
    # 获取模型类的返回值
    def get_model(self):
        return Post

    def index_queryset(self,using=None):
        return self.get_model().objects.order_by('-created')