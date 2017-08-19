#coding=utf-8
from django.http import HttpResponse,Http404
from django.template import loader
from django.shortcuts import render,render_to_response
import datetime


def home(request):

    return HttpResponse("<h1>my first html<h1>")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.<body><html>"%now
    return HttpResponse(html)

def bs(request):
    t = loader.get_template('bs.html')
    html = t.render({'time':datetime.datetime.now()})
    return HttpResponse(html)
    # time = datetime.datetime.now()
    # return render(request,'bs.html',locals())

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    html = "<html><body>In %s hours,it will be %s.<body><html>"%(offset,dt)
    return HttpResponse(html)

def sina(request,offset):
    if offset == "yingchao":
        return HttpResponse("英超界面")
    elif offset == "ouguan":
        return HttpResponse("欧冠界面")
    else:
        raise Http404()
