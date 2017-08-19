#coding=utf-8

from django.conf.urls import url
from view.views import *
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^test/(?P<offest>\d{1,2})/$',test),         #传参名字必须为offest,去掉什么都可以了
    url(r'^foo/$',foor_bar,{'template_name':'foo.html'}),
    url(r'^bar/$',foor_bar,{'template_name':'bar.html'}),

]

urlpatterns += [
    url(r'^about/$',TemplateView.as_view(template_name = 'about.html')),
    url(r'^go-to',RedirectView.as_view(url='/view/about')),     #可以跳转本地,也可以跳转外网
    url(r'^my_view',MyView.as_view()),
]
