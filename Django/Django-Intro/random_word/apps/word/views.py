from django.shortcuts import render, redirect
from time import strftime
from django.utils.crypto import get_random_string

# Create your views here.
def index(req):
    if 'count' not in req.session:
        req.session['count'] = 1
    data={
        'random':get_random_string(length=14),
        'count':req.session['count']
    }
    return render (req,'word/index.html',data)

def generate(request):
    if request.method == 'POST':
        request.session['count'] +=1
        return redirect('/')
    else:
        return redirect('/')

def reset(req):
    req.session.clear()
    return redirect('/')

# Create your views here.
