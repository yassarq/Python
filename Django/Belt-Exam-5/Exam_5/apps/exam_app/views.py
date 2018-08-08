from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from ..login_reg.models import User
from .models import Poke
from django.db.models import Count

root = 'poke_app:home'
login_root = 'login_reg:root'


def index(request):
    context = {
            # 'users' : User.objects.all()
        }
    return render(request, 'exam_app/index.html', context)


def register(request):
    check = User.userManager.register(request.POST['name'], request.POST['alias'], request.POST['email'], request.POST['password'], request.POST['confirm_pw'], request.POST['date_hired'])
    if (not check[0]):
        errors = []
        for key, value in check[1].iteritems():
            errors.append(value)
        context = {
            'errors' : errors
        }
        return render(request, 'index.html', context)
    else:
        request.session['id'] = User.objects.get(email=request.POST['email']).id
        return redirect('/')

def login(request):
    check = User.userManager.login(request.POST['email'], request.POST['password'])
    if (not check[0]):
        errors = [check[1]]
        context = {
            'errors' : errors
        }
        return render(request, 'index.html', context)
    else:
        request.session['id'] = User.objects.get(email=request.POST['email']).id
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def processingLogin(request, result):
    if result['status']:
        request.session['user_id'] = result['user_id']
        route = 'poke_app:home'
    else:
        for error in result['errors']:
            messages.error(request, error['message'])
        
def dashboard(request):
    if 'id' in request.session:
        context = {
        'may_poke': User.objects.filter(joins__id = request.session['id']),
        'notfriends':User.objects.exclude(joins__id = request.session['id']),
        }
        return render(request, 'exam_app/dashboard.html', context)
    else:
        return redirect('/')

def join(request, user_id):
    print(request.session['id'])
    User.objects.get(id = user_id).joins.add(User.objects.get(id = request.session['id']))

def poke(request,result):
    if result['status']:
        request.session['user_id'] = request['user_id']
        route = 'poke_app:home'
    else:
        for error in result['errors']:
            messages.error(request, error['message']), extra_tags = error['1 route = root']
        return route
    return redirect('/dashboard')

def home(request):
    if 'user_id' in request.session:
        uId = request.session['user_id']
        loggedUser = User.objects.get(id=uId)
        poked_by = loggedUser.pokes_recieved.all().value("poker__name")
        otherUsers = User.objects.exclude(id=uId)
        context = {
            'loggedUser': loggedUser,
            'otherUsers': otherUsers,
            'poked_by' : poked_by
        }


