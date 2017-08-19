# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404
from django.template import loader
import time
import datetime
from myapp.models import *      #导入models 数据库
from django.db.models import F,Q

def mydb(request):
    # # 增1
    # Author.objects.create(first_name = 'f',last_name = 'r',email = '2发的3@1cc.1')
    # Publisher.objects.create(name = '字符',address = 'huoxing',city = 'sase',state_province = 'yuzhou',country = 'shenniao',website = 'http.sxb.cn')
    # Book.objects.create(title = 'cvbc',publication_date = datetime.datetime.now(),publisher_id = 1)
    # #增2
    # obj = Author(first_name = 'Han',last_name = 'mei',email = 'hm@123.com')
    # obj.save()
    #
    # dic ={'first_name : 'Han','last_name' : 'mei','email' : 'hm@123.com'}
    # obj = Author(**dic)
    # obj.save()
    #
    # #删
    #Publisher.objects.filter(id__gt=2).delete()
    #
    # #改1
    # Author.objects.filter(id=4).update(first_name = 'lili')
    #
    # #改2
    # obj = Author.objects.get(id = 2)
    # obj.first_name = 'lucy'
    # obj.save()

    #查 select * from Author

    a = Author.objects.all()  #每一条记录生成一个对象
    # b = Author.objects.all().values('email')  #取出所有记录的指定字段
    # c = Author.objects.all().values_list('first_name','email')  #取出所有记录的指定字段
    # d = Author.objects.get(id = 1) #获取某一记录的对象
    # e = Author.objects.filter(id = 1)  #获取某一记录的对象


    # Author.objects.filter().update(age = F('age') + 1)          #更新默认值
    # return HttpResponse(e[0].email)

    # q = Q()
    #print dir(q)

    # q.connector = 'AND'
    # q.children.append(('id',4))
    # q.children.append(('last_name','mei'))
    #
    # f = Author.objects.filter(q)
    return HttpResponse("ok")
    # return HttpResponse(f[0].first_name)

def mtm(request):
    # book1 = Book.objects.get(id = 1)
    # s = book1.publisher.name
    # return HttpResponse(s)

    # pub1 = Publisher.objects.get(id = 2)
    # book_list = pub1.book_set.all()
    # return HttpResponse(book_list[2].publication_date)

    # author1 = Author.objects.get(id = 2)
    # book1_list = author1.book_set.all()
    # return HttpResponse(book1_list[0].title)

    # count = Book.myobjects.title_count('cvbc')
    # return HttpResponse(count)

    # author_list = book1.author.all()

    book2_list = Book.myobjects.all().little()

    return HttpResponse(book2_list)
