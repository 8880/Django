# -*- coding:utf-8 -*-
from django import forms


class RegForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username","required":"required"}),max_length=50,error_messages = {"required":"Username can not be empty"})
    password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password","required":"required"}),max_length=20,error_messages = {"required":"password can not be empty"})
    email=forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"Email","required":"required"}),max_length=50,error_messages = {"required":"Email can not be empty"})
    tel=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"telephone","required":"required"}),max_length=50,error_messages = {"required":"telephone can not be empty"})
