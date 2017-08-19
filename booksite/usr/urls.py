from django.conf.urls import *
from usr.views import *

urlpatterns = [
    url('^reg/$',reg,name = 'reg'),
    url('^login/$',login,name = 'login'),
    url('^loginout/$',loginout,name = 'loginout'),
    url('^thanks/$',login_test),
    url('^test/$',thanks),

]
