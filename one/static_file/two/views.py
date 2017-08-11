# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.contrib import auth
from forms import *
from django.contrib.auth.hashers import make_password
from django.db import connection
from django.db.models import Count
import time

# Create your views here.
def quanju(request):
    SITE_NAME = '微博'
    SITE_DESC = '微凉的晨露'
    category_list = Category.objects.all()
    tag_list = Tag.objects.all()
    archive_list = Article.objects.distinct_date()
    click_article_list = Article.objects.order_by('-click_count')[:4]
    recommend_article_list = Article.objects.all().filter(is_recommend = True)[:4]
    ad_list = Ad.objects.all()


    return locals()


def index(request):
    article_list = Article.objects.all()
    article_list = page(request, article_list)
    return render(request, 'index.html', locals())

def category(request):
    cid = request.GET.get('cid', None)
    category = Category.objects.get(id = cid)
    article_list = category.article_set.all()
    article_list = page(request, article_list)

    return render(request, 'category.html', locals())

def tag(request):
    cid = request.GET.get('tag', None)
    tag = Tag.objects.get(name = cid)
    article_list = tag.article_set.all()
    article_list = page(request, article_list)

    return render(request, 'tag.html', locals())

def article(request):
    # article_id = request.GET.get('id', None)
    # article = Article.objects.get(id = article_id)
    # return render(request, 'article.html', locals())

    try:
        # 获取文章id
        id = request.GET.get('id', None)
        try:
            # 获取文章信息
            article = Article.objects.get(pk=id)
            comment_list = article.comment_set.all()
            comment_counts = comment_list.count()
        except Article.DoesNotExist:
            return render(request, 'failure.html', {'reason': '没有找到对应的文章'})

        # 评论表单
        comment_form = CommentForm({'author': request.user.username,
                                    'email': request.user.email,
                                    'url': request.user.url,
                                    'article': id} if request.user.is_authenticated() else{'article': id})
        # 获取评论信息
        comments = Comment.objects.filter(article=article).order_by('id')
        comment_list = []
        for comment in comments:
            for item in comment_list:
                if not hasattr(item, 'children_comment'):
                    setattr(item, 'children_comment', [])
                if comment.pid == item:
                    item.children_comment.append(comment)
                    break
            if comment.pid is None:
                comment_list.append(comment)
    except Exception as e:
        print e
        logger.error(e)
    return render(request, 'article.html', locals())

def comment_post(request):
    try:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            #获取表单信息
            comment = Comment.objects.create(username=comment_form.cleaned_data["author"],
                                             email=comment_form.cleaned_data["email"],
                                             url=comment_form.cleaned_data["url"],
                                             content=comment_form.cleaned_data["comment"],
                                             article_id=comment_form.cleaned_data["article"],
                                             user=request.user if request.user.is_authenticated() else None)
            comment.save()
        else:
            return render(request, 'failure.html', {'reason': comment_form.errors})
    except Exception as e:
        logger.error(e)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def page(request,article_list):
    pa = Paginator(article_list, 3)
    try:
        p = int(request.GET.get('page', 1))
        article_list = pa.page(p)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        article_list = pa.page(1)
    return article_list

def ad(request):
    return render(request, 'ad.html', locals())

def archive(request):
    year = request.GET.get('year', None)
    month = request.GET.get('month', None)
    article_list = Article.objects.filter(date_publish__icontains=year+'-'+month)
    article_list = page(request, article_list)
    return render(request, 'archive.html', locals())

def login(request):
    errors=[]
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if not request.POST.get('username',''):
            errors.append('Enter a username.')
        if not request.POST.get('password',''):
            errors.append('Enter a password.')
        if not errors:
            if not request.user.is_authenticated():
                user = auth.authenticate(username=username,password=password)
                if user is not None and user.is_active:
                    auth.login(request,user)
                    return HttpResponseRedirect(request.POST.get('source_url'))

                else:
                    return HttpResponse('usrname or password invalid.')
            else:
                return HttpResponse("You have already login")
    return render(request,'login.html',{'errors':errors,})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def reg(request):
    try:
        if request.method == 'POST':
            reg_form = RegForm(request.POST)
            if reg_form.is_valid():
                cd = reg_form.cleaned_data
                User.objects.create(username=cd['username'], password=make_password(cd['password']), email=cd['email'], url=cd['url'])
                return render(request, 'login.html', locals())
            else:
                return render(request ,'failure.html', locals())
        else:
            reg_form = RegForm()
    except Exception as e:
        print e
    return render(request, 'reg.html', locals())
