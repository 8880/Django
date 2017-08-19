#coding=utf-8

from django.conf.urls import url
from myapp.views import *
from myapp.views1 import *

urlpatterns = [
    url(r'^first/$',first),
    url(r'^$',first),
    url(r'^bs/$',bs),
    url(r'^test/$',test),
    url(r'^template/$',temp),
    url(r'^meta/$',display_meta),
    url(r'^tags/$',tag),
    url(r'^filter/$',fil),
    url(r'^base/$',base,name='base'),
    url(r'^include/$',nav),
    url(r'^static/$',load),
    url(r'^fk/$',fk),
]
urlpatterns += [
    url(r'^model/$',mydb),
    url(r'^model1/$',mtm),
    url(r'^image/$',postImage),
    url(r'^message/$',message),
]
