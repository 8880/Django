# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from models import *
from forms import *
from django.contrib.auth.decorators import login_required,permission_required
from views import *
@login_required(login_url = '/login/')

def add(request):
    if request.method == 'POST':
        form = Add(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            dic = {
                'title': cd['title'],
                'desc': cd['desc'],
                'category': cd['category'],
                'tag': cd['tag'],
                'date_publish': cd['date_publish'],
                'content': cd['content'],
                'user': cd['user']}
            Article.objects.create(**dic)
            return HttpResponseRedirect('/')
    else:
        form = Add()
    return render(request, 'add.html', {'form': form})


def asd(request):
    if request.method == 'POST':
        form = Asd(request.POST)
        if form.is_valid():
            form.cleaned_data
            return HttpResponse("niubi!")
    else:
        form = Asd()
    return render(request, 'asd.html',{'form': form})
