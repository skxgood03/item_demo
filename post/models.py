from django.db import models

# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    cname = models.CharField(max_length=30,unique=True,verbose_name='类别名称')

    def __str__(self):
        return 'Category%s'%self.cname

# 后台admin改名字
    class Meta:
        verbose_name_plural='类别'

class Tag(models.Model):
    tname = models.CharField(max_length=30,unique=True,verbose_name='标签名称')

    def __str__(self):
        return 'Tag%s' % self.tname

    class Meta:
        verbose_name_plural='标签'

class Post(models.Model):
    title = models.CharField(max_length=100,unique=True)
    desc = models.CharField(max_length=100)
    content = RichTextUploadingField(null=True,blank=True)          #富文本
    created = models.DateTimeField(auto_now_add=True)
    categroy = models.ForeignKey(Category,on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return 'Post%s' % self.title

    class Meta:
        verbose_name_plural='帖子'