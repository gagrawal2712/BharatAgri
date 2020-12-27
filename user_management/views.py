from django.shortcuts import render
from django.http import HttpResponse
from user_management.http_views.sign_up import SignUp
from user_management.http_views.sign_in import SignIn, SignOut

# Create your views here.

def index(request):
    return HttpResponse("hello world")