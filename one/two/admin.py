# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *
class ArticleAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'desc', 'date_publish', 'category', 'is_recommend', 'click_count',)
    list_display_links = ('title', 'desc', )          #在对应列下可直接点击进入更改
    list_editable = ('click_count', 'is_recommend', 'category', )  #设置为模型上的字段名称列表，这将允许在更改列表页面上进行编辑。
    list_filter = ('date_publish','desc')     #过滤器
    search_fields = ('title', 'desc')       #搜索


    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )
class CommentAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )
# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Ad)
admin.site.register(User)
admin.site.register(Comment,CommentAdmin)
