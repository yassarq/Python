from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    context = {
            # 'users' : User.objects.all()
        }
    return render(request, 'exam_app/index.html', context)


def register(request):
    results = User.objects.regValidator(request.POST)
    if results[0] == True:
        request.session['id'] = results[0].id
        request.session['first_name'] = results[0].name
        return redirect('/dashboard')
    else:
        error_list = results[0]
        for error in error_list:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')


def dashboard(request):
    if 'id' in request.session:
        context = {
        'myfriends': User.objects.filter(joins__id = request.session['id']),
        'notfriends':User.objects.exclude(joins__id = request.session['id']),
        }
        return render(request, 'exam_app/dashboard.html', context)
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
    return render(request, 'exam_app/dashboard.html')

def show(request, user_id):
    context = {
        'user': User.objects.get(id = user_id),
        # 'joiners': User.objects.get(id = id).joins.all()

    }
    return render(request, 'exam_app/show.html', context)

def join(request, user_id):
    print(request.session['id'])
    User.objects.get(id = user_id).joins.add(User.objects.get(id = request.session['id']))

    return redirect('/dashboard')

def remove(request, user_id):
    User.objects.get(id = user_id).joins.remove(User.objects.get(id = request.session['id']))
    return redirect('/dashboard')
