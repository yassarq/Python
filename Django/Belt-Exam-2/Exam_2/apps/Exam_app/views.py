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
        context = {
        'mywishes':Wish.objects.filter(wisher_id=request.session['id']) | Wish.objects.filter(joiners__id = request.session['id']), 
        'otherwishes': Wish.objects.exclude(wisher_id = request.session['id']) & Wish.objects.exclude(joiners__id = request.session['id'])

        
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
    return render(request, 'exam_app/add.html')

def createitem(request):
    results = Wish.objects.itemValidator(request.POST,request.session['id'])
    if results[0] == True:
        return redirect('/dashboard')
    else:
        error_list = results[1]
        for error in error_list:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/add')

def show(request, id):
    context = {
        'item': Wish.objects.get(id = id),
        'joiners': Wish.objects.get(id = id).joiners.all()

    }
    return render(request, 'exam_app/show.html', context)

def join(request, item_id):
    Wish.objects.get(id = item_id).joiners.add(User.objects.get(id = request.session['id']))

    return redirect('/dashboard')

def remove(request, item_id):
    Wish.objects.get(id = item_id).joiners.remove(User.objects.get(id = request.session['id']))

    return redirect('/dashboard')

def delete(request, item_id):
    Wish.objects.get(id = item_id).delete()

    return redirect('/dashboard')