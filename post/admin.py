from django.contrib import admin

# Register your models here.

# 发帖设置时间
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','created')


from .models import *
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post,PostModelAdmin)
