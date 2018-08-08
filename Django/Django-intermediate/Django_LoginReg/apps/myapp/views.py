from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(req):
    context = {
        'users' : User.objects.all()
        }
    return render(req, 'myapp/index.html', context)

def process(req):

    action = req.POST['action']
    if action == "register":
        result = User.objects.regValidator(req.POST)
        print("receiving result")
        print(result)
        if result[0]:
            req.session['id'] = result[1].id
            req.session['name'] = result[1].fname
            return redirect("/success")
        else:
            error_list = result[1]
            for error in error_list:
                messages.add_message(req, messages.ERROR, error)
            return redirect('/')
    if action == "login":
                result = User.objects.loginValidator(req.POST)
                print("receiving result")
                print(result)

                if result[0]:
                    req.session['id'] = result[1].id
                    req.session['name'] = result[1].fname
                    return redirect("/success")
                else:
                    error_list = result[1]
                    for error in error_list:
                        messages.add_message(req, messages.ERROR, error)
                    return redirect('/')
    if action == "addproduct":
        result = Product.objects.productValidator(req.POST, req.session['id'])
        print("receiving result")
        print(result)
        if result[0]:
            return redirect("/success")
        else:
            error_list = result[1]
            for error in error_list:
                messages.add_message(req, messages.ERROR, error)
            return redirect('/success')

def success(req):


    if 'id' not in req.session:
        return redirect("/")
    else:
        products_notyet_sold = []
        mysales = []
        totalsales = 0
        totalpurchases = 0
        all_products = Product.objects.filter(seller_id = req.session['id'])
        for product in all_products:
            if len(Transaction.objects.filter(sale_id = product.id)) < 1:
                products_notyet_sold.append(product)
        all_sales = Transaction.objects.all()
        for i in all_sales:
            if i.id == req.session['id']:
                mysales.append(i)
        products_bought = Transaction.objects.filter(buyer_id=req.session['id'])
        for i in mysales:
            totalsales += i.sale.price
        for i in products_bought:
            totalpurchases += i.sale.price

        context = {

            'myproducts' : products_notyet_sold,
            'sales' : mysales,
            'purchases' : products_bought,
            'totalsales' : totalsales,
            'totalpurchases' : totalpurchases
        }

    return render(req, "myapp/success.html", context)


def clear(req):
    User.objects.all().delete()
    return redirect("/")

def logout(req):
    req.session.clear()
    return redirect("/")

def shoes(req):
    products_notyet_sold = []
    all_products = Product.objects.all()
    for product in all_products:
        if len(Transaction.objects.filter(sale_id = product.id)) < 1:
            products_notyet_sold.append(product)

    products_sold = Transaction.objects.filter()    
    context = {

        'products' : products_notyet_sold,
        'sale' : products_sold

    }

    return render(req, "myapp/shoes.html", context)

def buy(req, sale_id):

    Transaction.objects.create(buyer_id=req.session['id'],sale_id=sale_id)


    # sale = models.ForeignKey(Product, related_name="sold")
    # buyer = models.ForeignKey(User, related_name="bought")

    return redirect("/shoes")

def remove(req, product_id):

    Product.objects.get(id = product_id).delete()

    return redirect("/success")
