from django.urls import path

from post import views

urlpatterns=[
    path('',views.queryAll),
    path('page/<int:num>',views.queryAll),   #分页
    path('post/<int:postid>',views.detail),    #阅读全文
    path('category/<int:cid>',views.QueryPost),    #分类查询
    path('archive/<int:year>/<int:month>',views.querycreate),    #日期查询
]