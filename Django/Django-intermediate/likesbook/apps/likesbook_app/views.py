from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):

    return render(request, 'likesbook_app/index.html')

def process(request): # (Step 1)
    # print(request.POST) # (Step 2)

    action = request.POST['action']

    if action == "register":

        result = User.objects.regValidator(request.POST)

        if result[0]:

            request.session['id'] = result[1].id # (Step 10)
            request.session['name'] = result[1].fname

            return redirect("/success")

        else:
            error_list = result[1]
            for error in error_list:
                messages.add_message(request, messages.ERROR, error) # (Step 11)

            return redirect('/')

    if action == "login":

        result = User.objects.loginValidator(request.POST)

        if result[0]:

            request.session['name'] = result[1].fname
            request.session['id'] = result[1].id
            return redirect("/success")

        else:
            error_list = result[1]
            for error in error_list:
                messages.add_message(request, messages.ERROR, error)

            return redirect('/')

def processbook(request):

    action = request.POST['action']

    if action == "addbook":

        result = Book.objects.bookValidator(request.POST, request.session['id'])
        print(result)
        if result[0]:

            request.session['id'] = result[1].id
            request.session['bookname'] = result[1].bookname
            error_list = result[2]
            for error in error_list:
                messages.add_message(request, messages.ERROR, error)
            return redirect("/success")

        else:
            error_list = result[1]
            for error in error_list:
                messages.add_message(request, messages.ERROR, error)

            return redirect('/success')

def success(req):

    if 'id' not in req.session:
        return redirect("/")
    else:
        
        context = {
            'books' : Book.objects.all()
        }
    return render(req, "likesbook_app/success.html", context)

def likedbook(req, id):

    b1 = Book.objects.get(id = id)
    b1.readers.add(User.objects.get(id=req.session['id']))

    return redirect('/success')


def clear(request):
    User.objects.all().delete()
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

