from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.
def index(req):
    print(datetime.now())
    if 'wordlist' not in req.session:
        req.session['wordlist'] = []
    context = {
        'wordlist': req.session['wordlist']
    }
    print(req.session['wordlist'])
    return render(req, 'words/session.html', context )

def add_word(req):
    print(req.POST)
    word = req.POST['word']
    if 'color' in req.POST:
        color = req.POST['color']
    else:
        color = 'black'
    if 'isbig' in req.POST:
        isbig = req.POST['isbig']
    else:
        isbig = 'NO'

    templist = req.session['wordlist']
    templist.insert(0,{
        'word': word,
        'color': color,
        'isbig': isbig,
        'time' : str(datetime.now())
    })
    req.session['wordlist'] = templist
    return redirect('/')

def clear(req):
    req.session.clear()
    return redirect('/')

