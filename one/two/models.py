# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200, blank=True, null=True, verbose_name='用户头像')
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ号码')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')
    url = models.URLField(max_length=100, blank=True, null=True, verbose_name='个人网页地址')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username

class ArticleManager(models.Manager):
    def distinct_date(self):
        distinct_date_list = []
        date_list = self.values('date_publish')
        for date in date_list:
            date = date['date_publish'].strftime('%Y/%m') + "文章存档"
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list

class Category(models.Model):
    name = models.CharField(max_length = 30, verbose_name = '分类名称')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

class Tag(models.Model):
    name = models.CharField(max_length = 30, verbose_name = '标签名称')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

class Article(models.Model):
    title = models.CharField(max_length = 100, verbose_name = '标题')
    desc = models.CharField(max_length = 200, verbose_name = '副标题')
    date_publish = models.DateField(blank = True, null = True, verbose_name = '发布时间')
    click_count = models.IntegerField(null = True, default = 0, verbose_name = '浏览量')
    is_recommend = models.BooleanField(default=False, verbose_name = '是否推荐')
    user = models.ForeignKey(User, verbose_name='用户')
    content = models.TextField(null = True, blank = True, verbose_name = '文章内容')
    category = models.ForeignKey(Category, null=True, verbose_name='分类')
    tag = models.ManyToManyField(Tag)

    objects = ArticleManager()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-id']

class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    username = models.CharField(max_length=30, blank=True, null=True, verbose_name='用户名')
    email = models.EmailField(max_length=50, blank=True, null=True, verbose_name='邮箱地址')
    url = models.URLField(max_length=100, blank=True, null=True, verbose_name='个人网页地址')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.ForeignKey(User, blank=True, null=True, verbose_name='用户')
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name='文章')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str(self.id)

class Ad(models.Model):
    image_url = models.ImageField(upload_to='ad/%Y/%m', verbose_name='图片路径')
    callback_url = models.URLField(null = True, blank = True, verbose_name = '链接地址')
    description = models.CharField(max_length = 100, verbose_name = '照片描述')

    def __unicode__(self):
        return self.description

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = verbose_name
