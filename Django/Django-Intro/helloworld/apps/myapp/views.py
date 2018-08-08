from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(req):
    return render(req, 'myapp/index.html')

def new(req):
    return render(req, 'myapp/index.html')

def index2(req):
    response = "Hello, I am your first request!"
    return HttpResponse("placeholder to later display all the list of blogs")