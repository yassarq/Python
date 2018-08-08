from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):

    return render(request, 'exam_app/index.html')

def process(request): # (Step 1)
    # print(request.POST) # (Step 2)

    action = request.POST['action']

    if action == "register":

        result = User.objects.regValidator(request.POST)

        if result[0]:

            request.session['id'] = result[1].id # (Step 10)
            request.session['name'] = result[1].name

            return redirect("/success")

        else:
            error_list = result[1]
            for error in error_list:
                messages.add_message(request, messages.ERROR, error) # (Step 11)

            return redirect('/')

    if action == "login":

        result = User.objects.loginValidator(request.POST)

        if result[0]:

            request.session['name'] = result[1].name
            request.session['id'] = result[1].id
            return redirect("/success")

        else:
            error_list = result[1]
            for error in error_list:
                messages.add_message(request, messages.ERROR, error)

            return redirect('/')
def processquote(request):
    
    action = request.POST['action']

    if action == "addquote":

        result = Quote.objects.quoteValidator(request.POST, request.session['id'])
        print(result)
        if result[0]:

            # request.session['quote_id'] = result[1].id
            request.session['quotename'] = result[1].quotename
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
            'quote' : Quote.objects.all(),
            'creator' : User.objects.all()
        }
    return render(req, "exam_app/success.html", context)


def likedquote(req, id):

    b1 = Quote.objects.get(id = id)
    b1.likers.add(User.objects.get(id=req.session['id']))

    return redirect('/success')


def clear(request):
    User.objects.all().delete()
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def show(request, poster_id):
    context = {
        'user':User.objects.get(id= poster_id),
        'joiners':Quote.objects.filter(likers__id = poster_id)
    }
    return render(request, 'exam_app/show.html', context)

def join(request, item_id):
    Quote.objects.get(id = item_id).likers.add(User.objects.get(id = request.session['id']))

    return redirect('/dashboard')

def remove(request, item_id):
    Quote.objects.get(id = item_id).likers.remove(User.objects.get(id = request.session['id']))

    return redirect('/dashboard')
