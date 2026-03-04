from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("hello from mysite 😂")
# Create your views here.
