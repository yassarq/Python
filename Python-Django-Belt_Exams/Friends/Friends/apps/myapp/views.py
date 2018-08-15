from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    context = {
            # 'users' : User.objects.all()
        }
    return render(request, 'myapp/index.html', context)


def register(request):
    results = User.objects.regValidator(request.POST)
    if results[0] == True:
        request.session['id'] = results[1].id
        request.session['first_name'] = results[1].name
        return redirect('/dashboard')
    else:
        error_list = results[1]
        for error in error_list:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')

def dashboard(request):
    if 'id' in request.session:
        # user1 = User.objects.get(id=1)
        # user5 = User.objects.get(id=5)
        # user3 = User.objects.get(id=3)
        # user1.joins.add(user5)
        # user1.joins.add(user3)
        # user5.joins.add(user1)
        context = {
        'notfriend': User.objects.exclude(joins__id = request.session['id']),
        'friend':User.objects.filter(joins__id = request.session['id']),
        # 'joins_of_user1':user1.joins.all(),
        # 'joins_of_user3':user3.joins.all(),
        # 'joins_of_user5':user5.joins.all(),
        }
        return render(request, 'myapp/dashboard.html', context)
    else:
        return redirect('/')

def login(request):
    results = User.objects.loginValidator(request.POST)
    if results[0] == True:
        request.session['id'] = results[1].id
        request.session['first_name'] = results[1].name
        return redirect('/dashboard')
    else:
        error_list = results[1]
        for error in error_list:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def add(request):
    return render(request, 'myapp/dashboard.html')


def show(request, user_id):
    context = {
        'user':User.objects.get(id= user_id),
        'joiners': User.objects.filter(joins__id = user_id)
    }
    return render(request, 'myapp/show.html', context)

def join(request,user_id):
    User.objects.get(id = user_id).joins.add(User.objects.get(id = request.session['id']))

    return redirect('/dashboard')

def remove(request, user_id):
    User.objects.get(id =user_id).joins.remove(User.objects.get(id = request.session['id']))

    return redirect('/dashboard')
