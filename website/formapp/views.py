# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from formapp.forms import *
from myapp.models import *
# Create your views here.
def search_form(request):
    return render(request,'search_form.html',{})

def search(request):
    print request.GET
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        return HttpResponse("I have get the '%s'"%q)
    else:
        return render(request,'search_form.html',{'error':True})

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject',''):
            errors.append('请输入主题')

        if not request.POST.get('email',''):
            errors.append('请输入邮箱')

        if not request.POST.get('message',''):
            errors.append('请输入内容')

        if not errors:
            #return HttpResponseRedirect("/form/contact/thanks")
            return redirect("/form/contact/thanks")

    return render(request,"contact_form.html",{'errors':errors,'subject':request.POST.get('subject'),'email':request.POST.get('email'),'message':request.POST.get('message')})

def thanks(request):
    #print 'come on'
    return HttpResponse("成功!")
    #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))           #执行后跳回原页面


def formtest(request):
    if request.method == 'POST':
        form = RemarkForm(request.POST)
        if form.is_valid():              # is_valid()方法来执行验证并返回一个表示数据是否合法的布尔值
            cd = form.cleaned_data     # 填充的是目前为止已经合法的数据。
            print cd['subject']
            print cd['mail']
            print cd['topic']
            print cd['message']
            print cd['cc_myself']
            return HttpResponseRedirect('/form/form')
    else:
        form = RemarkForm()

    return render(request,'formset.html',{'form':form})

def bookset(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            cd  = form.cleaned_data
            dic = {'first_name':cd['first_name'],'last_name':cd['last_name'],'age':cd['age'],'email':cd['email']}
            Author.objects.create(**dic)
            return HttpResponseRedirect('/form/bookform')
    else:
        form = AuthorForm()

    return render(request,'bookset.html',{'form':form})


user_info = {
    'kun': {'pwd': 'kun123'},
    'kangbazi': {'pwd': '123456'},
}

# @csrf_exempt
# def login(request):
#     if request.method == 'GET':
#         return render(request, "login.html")
#     if request.method == 'POST':
#         u = request.POST.get('username')
#         p = request.POST.get('pwd')
#         dic = user_info.get(u)
#         if not dic:
#             return render(request, 'login.html')
#         if dic['pwd'] == p:
#             res = redirect("/form/index/")
#             res.set_cookie('user',u)
#             return res
#         else:
#             return render(request, 'login.html')
#
# def index(request):
#     v = request.COOKIES.get('user')
#     if not v:
#         return redirect('/form/login/')
#     return render(request, 'index.html', {'current_user': v})


# @csrf_exempt
# def login(request):
#     if request.method == 'GET':
#         return render(request, "login.html")
#     if request.method == 'POST':
#         u = request.POST.get('username')
#         p = request.POST.get('pwd')
#         if u == 'root' and p == '123':
#             request.session['username'] = u
#             request.session['is_login'] = True
#             request.session.set_expiry(10)
#             return redirect("/from/index/")
#         else:
#             return render(request, 'login.html')
#
# def index(request):
#     if request.session.get('is_login', None):
#         return render(request, 'index.html', {'current_user': request.session['username']})
#     else:
#         return render(request, 'login.html')
# def logout(request):
#     print dir(request.session)
#     request.session.clear()
#     return redirect("/form/login")
