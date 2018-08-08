from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from apps.poke.models import User, Poke
from django.utils import timezone
from datetime import datetime
from django.db.models import Count


def index(request):
	print (request.GET)
	print (request.method)
	return render(request, 'poke/index.html')

def register(request):
	print ("Registration")
	user = User.objects.filter(email=request.POST.get('email'), password = request.POST.get('password'))
	errors = []
	successes = []
	if len(request.POST.get('first_name')) < 4:
		errors.append('First name must be at least 4 characters.')
	if len(request.POST.get('last_name'))<4:
		errors.append('Last name must be at least 4 characters.')
	if not "@" in request.POST.get('email') or len(request.POST.get('email'))<8:
		errors.append('Must enter a valid email. Email must be at least 8 characters.')
	if len(request.POST.get('password'))<4:
		errors.append('Password must be at least 4 characters.')
	if len(user) > 0:
		errors.append('This user already exists!')
	if not errors:
		user = User()
		user.first_name = request.POST.get('first_name')
		user.last_name = request.POST.get('last_name')
		user.email = request.POST.get('email')
		user.description = request.POST.get('description')
		user.password = request.POST.get('password')
		user.created_at = timezone.now()
		user.save()
		successes.append('You have successfully registered and may login!')
		print ("Successful Registration")
		print (user.first_name)
		print (user.last_name)
		print (user.email)
		print (user.password)
		return render(request, 'poke/index.html', {'successes': successes})
	else:
		del request.session
		return render(request, 'poke/index.html', {'errors': errors})


def login(request):
	print ("Login")
	log_errors = []
	print (request.POST.get('email'))
	print (request.POST.get('password'))
	user = User.objects.filter(email=request.POST.get('email'), password=request.POST.get('password'))
	if len(user)<1:
		log_errors.append("This user doesn't exist")
		return render(request, 'poke/index.html', {'log_errors': log_errors})
	else:
		print ("Success")
		request.session['user_id'] = user[0].id
		print ("Logging In..")
		return redirect('/dashboard')

def dashboard(request):
	print ("User Dashboard")
	if "user_id" in request.session:
		users = User.objects.all().exclude(id=request.session['user_id'])
		pokes = Poke.objects.all().distinct('poked_id')
		user_poke_count = Poke.objects.all().filter(poked=request.session['user_id'])
		list_of_users = Poke.objects.filter(poked=request.session['user_id']).exclude(id=request.session['user_id']).distinct('poker')
		user = User.objects.get(id=request.session['user_id'])
		current_user = User.objects.get(id=request.session['user_id'])
		context = {'current_user': current_user,'user': user, 'users': users, 'pokes': pokes, 'user_poke_count': user_poke_count, 'list_of_users': list_of_users }
		return render(request, 'poke/dashboard.html', context)
	else:
		del request.session
		return redirect('/')

def poke(request, user_id):
	poker = User.objects.get(id=request.session['user_id'])
	print (poker.first_name)
	poked = User.objects.get(id=user_id)
	print (poked.first_name)
	poke = Poke()
	poke.poker = poker
	poke.poked = poked
	poke.created_at = timezone.now()
	poke.counter+=1
	poke.save()
	return redirect('/dashboard')

def logout(request):
	print ("Logging Out")
	del request.session['user_id']
	return redirect('/')