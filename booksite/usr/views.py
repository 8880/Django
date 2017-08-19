from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
#from django.template import RequestContext
from forms import *
from usr.models import *
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.

@permission_required('add_User',login_url = '/login/')
def thanks(request):
    return HttpResponse("Thanks for your register")

#@permission_required(login_url = '/thanks/')
def reg(request):
    try:
        if request.method == 'POST':
            reg_form = RegForm(request.POST)
            if reg_form.is_valid():
                cd = reg_form.cleaned_data
                User.objects.create(username=cd['username'],password=make_password(cd['password']),email=cd['email'],mobile=cd['tel'])

                return HttpResponseRedirect("/login/")
            else:
                return render(request,'failure.html',{'reason':reg_form.errors})
        else:
            reg_form = RegForm()
    except Exception as e:
        print e
    return render(request,'reg.html',locals())


@login_required(login_url = '/login/')
def login_test(request):
    return HttpResponse('Thank you for login')

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
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

                else:
                    return HttpResponse('usrname or password invalid.')
            else:
                return HttpResponse("You have already login")
    return render(request,'user_login.html',{'errors':errors,})

def loginout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")
