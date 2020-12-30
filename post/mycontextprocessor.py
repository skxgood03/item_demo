# coding=utf-8
from django.db.models import Count
# 全局上下文
from post.models import Post
from django.db import connection

def getRightInfo(request):
    #获取分类信息
    r_catepost = Post.objects.values('categroy__cname','categroy').annotate(c=Count('*')).order_by('-c')
    # 近期文章
    r_recpost = Post.objects.all().order_by('-created')[:3]

    # 获取归档日期
    cursor = connection.cursor()
    cursor.execute("select created,count('*') from post_post GROUP BY DATE_FORMAT( created,'%Y-%m')")
    r_file = cursor.fetchall()

    return {'r_catepost':r_catepost,'r_recpost':r_recpost,'r_file':r_file}