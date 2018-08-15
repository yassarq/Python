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
        user1 = User.objects.get(id=1)
        user5 = User.objects.get(id=5)
        user3 = User.objects.get(id=3)
        user1.joins.add(user5)
        user1.joins.add(user3)
        user5.joins.remove(user1)
        context = {
        'otherquotes': List.objects.exclude(favorites__id = request.session['id']),
        'myquotes':List.objects.filter(favorites__id = request.session['id']),
        'joins_of_user1':user1.joins.all(),
        'joins_of_user3':user3.joins.all(),
        'joins_of_user5':user5.joins.all(),
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

def createitem(request):
    results = List.objects.quoteValidator(request.POST,request.session['id'])
    if results[0] == True:
        return redirect('/dashboard')
    else:
        error_list = results[1]
        for error in error_list:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/dashboard')

def show(request, poster_id):
    context = {
        'user':User.objects.get(id= poster_id),
        'joiners':List.objects.filter(favorites__id = poster_id)
    }
    return render(request, 'exam_app/show.html', context)

def join(request, item_id):
    List.objects.get(id = item_id).favorites.add(User.objects.get(id = request.session['id']))

    return redirect('/dashboard')

def remove(request, item_id):
    List.objects.get(id = item_id).favorites.remove(User.objects.get(id = request.session['id']))

    return redirect('/dashboard')
