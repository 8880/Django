# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from myapp.models import *

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','id')  #显示项
    search_fields = ('first_name','last_name')          #搜索

class BookAdmin(admin.ModelAdmin):
    list_filter = ('publication_date',)    #过滤器
    date_hierarchy = 'publication_date'     #根据时间过滤
    ordering = ('-publication_date',)       #根据时间排序
    fields = ('title','author','publisher','publication_date')   #注册条目排序
    list_display = ('title','publication_date','publisher_id','id')  #显示项

admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Ad)
