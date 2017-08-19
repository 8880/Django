from django.conf.urls import url
from django.contrib import admin
from views import *
from views1 import *

urlpatterns = [
    url(r'^$', index),
    url(r'^category/$',category, name='category'),
    url(r'^tag/$', tag, name='tag'),
    url(r'^article/$', article, name='article'),
    url(r'^ad/$', ad, name='ad'),
    url(r'^archive/$', archive, name='archive'),
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^reg/$', reg, name='reg'),
    url(r'^comment/post/$', comment_post, name='comment_post'),
    url(r'^add/$', add, name='add'),
    url(r'^asd/$', asd, name='asd')
]
