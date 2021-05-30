from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')  # 给content字段添加富文本
    list_display = ['article_id', 'title', 'created_time']
    search_fields = ['title']  # 搜索框
    list_filter = ['created_time']  # 过滤器


#ass ArticleAdmin(admin.ModelAdmin):
class CommentAdmin(admin.ModelAdmin):
    list_display = ['username', 'body', 'title']
    search_fields = ['title']  # 搜索框


admin.site.register(models.User)
admin.site.register(models.Article)