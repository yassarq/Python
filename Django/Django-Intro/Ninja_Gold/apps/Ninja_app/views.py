from django.shortcuts import render, redirect
from datetime import datetime
import random
# Create your views here.

def index(req):
    if 'gold' not in req.session:
        req.session['gold'] = 0
    if 'activities' not in req.session:
        req.session['activities'] = []
    return render(req, "Ninja_app/index.html", )


def process_money(req):
    red='red'
    green='green'
    now = datetime.now()
    if 'farm' in req.POST:
        color = 'green'
        gold = random.randint(10, 21)
        activity = "Farmed for " + str(gold) + " gold" + str(now)
    if 'cave' in req.POST:
        color = 'green'
        gold = random.randint(5, 11)
        activity = "Carved for " + str(gold) + " gold" + str(now)
    if 'house' in req.POST:
        color = 'green'
        gold = random.randint(2, 6)
        activity = "Chored for " + str(gold) + " gold" + str(now)
    if 'casino' in req.POST:
        gold = random.randint(-50, 51)
        if gold > 0:
            color = 'green'
            activity = "Gambled and won " + str(gold) + " gold" + str(now)
        if gold < 0:
            color = 'red'
            activity = "Gambled and lost " + str(gold) + " gold" + str(now)
    req.session['gold'] += gold
    temp_list = req.session['activities']
    temp_list.append({
        'activity':activity,
        'color':color
        })
    req.session['activities'] = temp_list

    return redirect("/")

def reset(req):
    req.session.clear()
    return redirect("/")




