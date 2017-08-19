# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    avater = models.ImageField(default = 'static/default.jpg',max_length = 200,blank = True,null = True,verbose_name = '头像')
    mobile = models.CharField(max_length = 11,blank = True,null = True,verbose_name = '手机')
    class Meta:
        verbose_name = '用户'
        ordering = ['-id']
    def __unicode__(self):
        return self.username
