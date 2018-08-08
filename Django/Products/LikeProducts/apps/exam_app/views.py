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
def processproduct(request):
    
    action = request.POST['action']

    if action == "addproduct":

        result = Product.objects.productValidator(request.POST, request.session['id'])
        print(result)
        if result[0]:

            # request.session['product_id'] = result[1].id
            request.session['productname'] = result[1].productname
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
            'product' : Product.objects.all(),
            'creator' : User.objects.all()
        }
    return render(req, "exam_app/success.html", context)

def likedproduct(req, id):

    b1 = Product.objects.get(id = id)
    b1.likers.add(User.objects.get(id=req.session['id']))

    return redirect('/success')


def clear(request):
    User.objects.all().delete()
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')