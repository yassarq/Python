from django.shortcuts import render, redirect

# Create your views here.
def index(req):
    return render(req, 'forth_app/Survey_form.html')

def success(req):
    return render(req, 'forth_app/success.html')

def process(req):
    # print(req.POST['location'])
    req.session['name']=req.POST['name']
    req.session['language']=req.POST['language']
    req.session['location']=req.POST['location']
    req.session['comment1']=req.POST['comment2']
    return redirect('/success')
    