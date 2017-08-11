# -*- coding:utf-8 -*-
from django import forms
from django.conf import settings
from django.db.models import Q
from models import *
import re

class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "required": "required",}),
                              max_length=50,error_messages={"required": "username不能为空",})
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "required": "required",}),
                              max_length=20,error_messages={"required": "password不能为空",})


class RegForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "required": "required",}),
                              max_length=50,error_messages={"required": "username不能为空",})
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Email", "required": "required",}),
                              max_length=50,error_messages={"required": "email不能为空",})
    url = forms.URLField(widget=forms.TextInput(attrs={"placeholder": "Url", }),
                              max_length=100, required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "required": "required",}),
                              max_length=20,error_messages={"required": "password不能为空",})

class CommentForm(forms.Form):
    author = forms.CharField(widget=forms.TextInput(attrs={"id": "author", "class": "comment_input", "required": "required", "size": "25", "tabindex": "1"}), max_length=50, error_messages={"required": "username不能为空",})
    email = forms.EmailField(widget=forms.TextInput(attrs={"id": "email", "type": "email", "class": "comment_input", "required": "required", "size": "25", "tabindex": "2"}), max_length=50, error_messages={"required": "email不能为空"})
    url = forms.URLField(widget=forms.TextInput(attrs={"id":"url","type":"url","class": "comment_input","size":"25", "tabindex":"3"}),max_length=100, required=False)
    comment = forms.CharField(widget=forms.Textarea(attrs={"id":"comment","class": "message_input","required": "required", "cols": "25","rows": "5", "tabindex": "4"}),error_messages={"required":"评论不能为空",})
    article = forms.CharField(widget=forms.HiddenInput())

class Add(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        labels = {
            'title': '主题',
            'desc': '副标题',
            'category': '分类',
            'date_publish': '发布时间',
            'content': '文章内容',
        }


class Asd(forms.Form):
    name = forms.CharField(max_length = 50, label = '名字')
    message = forms.CharField(label = '内容', widget = forms.Textarea)
