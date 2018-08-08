from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string


def index(request):
    context = {
        "email" : "blog@gamil.com",
        "name"  : "mike"
    }



    return render (request, "myapp/index.html",context)

from django.shortcuts import render, HttpResponse, redirect
def create(request):
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print(request.POST['name'])
        print(request.POST['desc'])
        request.session['name'] = "test"  # more on session below
        print("*"*50)
        request.session['name'] = request.POST['name']
        request.session['counter'] = 100
        return redirect("/")
    else:
        return redirect("/")


