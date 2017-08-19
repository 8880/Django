# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404
from django.template import loader
import time

# Create your views here.

def global_setting(request):        #全局变量
    NAME = 'cainiao'
    TEL = '18810207835'
    GEYAN = 'hhhhh'
    return locals()

def fun():
    return "hello"

class A(object):
    a = "class -> a"
    def f(self):
        return "jest a A:fun"


def first(request):
    return HttpResponse("my first app")

def bs(request):
    t = loader.get_template('bs.html')
    html = t.render({})
    return HttpResponse(html)

def test(request):
    #return render_to_response('bs.html',{})
    return render(request,'bs.html',{})

def temp(request):
    t = time.localtime()
    return render(request,'time.html',{'datetime':t})
    #return render(request,'time.html',locals())

def display_meta(request):
    num = 1
    s = "hello"
    l = [1,2,'c','nihao']
    t = (4,5,'d','tuple')
    d = {'a':'one','b':'two','c':'three'}
    f = fun()
    obj = A()

    return render(request,'meta.html',\
    {'num':num,'s':s,'list':l,'tuple':t,'dict':d,'fun':f,'obj':obj})
    # return render(request,'meta.html',locals())

def tag(request):
    l = [1,2,3,4,5]
    return render(request,'tags.html',{'error':"",'list':l})             #error不是空值为真,""与0会执行错误语句,此外执行成功语句

def fil(request):
    num = 1
    s = 'HELLO WORLD'
    return render(request,'filter.html',{'num':num,'s':s})

def base(request):
    return render(request,'1.html',{})

def nav(request):
    return render(request,'nav.html',{})

def load(request):
    return render(request,'static.html',{})

def fk(request):
    return render(request,'fk.html',{})

def postImage(request):
    return render(request,'image.html',{})

def message(request):
    try:
        img = Ad(title = "imgTest",img = request.FILES.get('picfile'))
        img.save()
    except Exception,e:
        return HttpResponse("Error:%s"%e)
    return HttpResponse("post images")

# def message(request):
#     try:
#         imgFile = request.FILES['picfile']
#         img = Image.open(imgFile)
#         img.save("/home/linux/djangosite/website/media/a.png",'png')
#     except Exception,e:
#         return HttpResponse("Error:%s"%e)
#     return HttpResponse("post images")
