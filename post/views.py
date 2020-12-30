import math

from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# 渲染主页面
from post.models import Post,Tag,Category
from django.core.paginator import Paginator


def queryAll(request,num=1):
    num = int(num)
    # 获取所有帖子信息并排序
    postlist = Post.objects.all().order_by('-created')
    # 创建分页器对象
    pageobj = Paginator(postlist,1)
    # 获取当前页的数据
    perpageList = pageobj.page(num)
    # 生成页码数的列表
    # 每页开始页码
    begin = (num -int(math.ceil(10.0/2)))
    if begin < 1:
        begin = 1
    # 每页结束页码
    end = begin + 9
    if end >pageobj.num_pages:
        end = pageobj.num_pages

    if end <=10:
        begin = 1
    else:
        begin = end - 9
    pageList = range(begin,end+1)
    return render(request, "index.html",{'postlist':perpageList,'pageList':pageList,'num':num})

# 阅读全文功能
def detail(request,postid):
    postid=int(postid)
    # 根据postid 来查询帖子的详情信息
    post = Post.objects.get(id=postid)
    return render(request,"detail.html",{'post':post})


def QueryPost(request,cid):
    cursor = connection.cursor()
    cursor.execute("SELECT id, title,created  FROM post_post WHERE categroy_id ={}".format(cid))
    postlist = cursor.fetchall()
    print(postlist)
    return render(request,"article.html",{'postlist':postlist})


def querycreate(request,year,month):
    cursor = connection.cursor()
    cursor.execute("SELECT id, title,created FROM post_post WHERE DATE_FORMAT(created ,'%Y')= {} and DATE_FORMAT(created ,'%m')={}".format(year,month))
    postlist = cursor.fetchall()
    print(postlist)
    return render(request,"article.html",{'postlist':postlist})



