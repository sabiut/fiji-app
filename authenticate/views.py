
import socket
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from fijiApi.models import Villages


def index(requests):
    return render(requests,'index.html')

def loginpage(request):
    return render(request, 'login.html')


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/dashboard')
    else:
         return HttpResponseRedirect('/invalid_page')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/loginpage')

def invalid_page(request):
    return render(request, 'invalid.html')


