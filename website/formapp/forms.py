#coding=utf-8
from django import forms
from myapp.models import *

TOPIC_CHOICES = (
    ('leve1','好评'),
    ('leve2','中评'),
    ('leve3','差评'),
)

class RemarkForm(forms.Form):
    subject = forms.CharField(max_length = 100,label = '标题')
    mail = forms.EmailField(label = '邮件')
    topic = forms.ChoiceField(choices = TOPIC_CHOICES,label = '评价')
    message = forms.CharField(label = '内容',widget = forms.Textarea)
    cc_myself = forms.BooleanField(required = False,label = '订阅')

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        labels = {
            'first_name':'姓',
            'last_name':'名',
            'email':'电子邮件',
            'age':'年龄',
        }
