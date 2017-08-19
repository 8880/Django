# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BookQuerySet(models.QuerySet):
    def little(self):
        return self.filter(id__lt = 6)

class BookManager(models.Manager):
    def get_queryset(self):
        return BookQuerySet(self.model,using=self._db)

    def title_count(self,keyword):
        return self.filter(title__icontains = keyword).count()


class Publisher(models.Model):                       #填写完表结构在终端输入同步命令同步到数据库
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 60)
    state_province = models.CharField(max_length = 30)
    country = models.CharField(max_length = 50)
    website = models.URLField(verbose_name = '网址')

    def __unicode__(self):
        return self.name             #改变组名,用改组的name显示

    class Meta:
        db_table = 'publisher'         #在mysql改变列表名称
        ordering = ['name']             #按name进行排序 -相反
        verbose_name = '出版社'          #改变类名
        verbose_name_plural = verbose_name   #去掉名字后的s

class Author(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 40)
    email = models.EmailField(blank = True)
    age = models.IntegerField(null = True,default = 10)

    def __unicode__(self):
        return '%s %s'%(self.first_name,self.last_name)

class Book(models.Model):
    title = models.CharField(max_length = 100,verbose_name = '书名')
    publication_date = models.DateField(blank = True,null = True)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    objects = models.Manager()
    myobjects = BookManager()

    def __unicode__(self):
        return self.title   #改变组名

        class Meta:
            ordering = ['title']      #按title排序
            
class Ad(models.Model):
    title = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = "avatar/%Y/%m",default = 'a.png', verbose_name='用户头像')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
