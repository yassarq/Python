from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):

    def regValidator(self, form):

        errors = []

        fname = form['fname']
        lname = form['lname']
        email = form['email'].lower()
        password = form['password']
        confirm_pw = form['confirm_pw']

        if not fname:
            errors.append("First name is required.")
        elif len(fname) < 3:
            errors.append("First name must be at least 3 characters.")
        elif not fname.isalpha():
            errors.append("First name cannot contain numbers.")
        if not lname:
            errors.append("Last name is required.")
        elif len(lname) < 3:
            errors.append("Last name must be at least 3 characters.")
        elif not lname.isalpha():
            errors.append("Last name cannot contain numbers.")
        if not email:
            errors.append("Email is required.")
        elif not EMAIL_REGEX.match(email):
            errors.append("Invalid Email")
        else:
            users = User.objects.filter(email = email)
            if users:
                errors.append("Email already exists. Please login.")
        if not password:
            errors.append("Password is required.")
        if not confirm_pw:
            errors.append("Confirm password is required.")
        if password != confirm_pw:
            errors.append("Passwords must match.")

        if not errors:
            # save user in database
            hash_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = User.objects.create(fname=fname, lname=lname, email=email, password=hash_pw)
            return (True, user)
        else:
            return (False, errors)


    def loginValidator(self, form):
        errors = []

        email = form['email'].lower()
        password = form['password']

        if not email:
            errors.append("Email is required.")
        elif not EMAIL_REGEX.match(email):
            errors.append("Invalid Email")
        else:
            users = User.objects.filter(email = email)
            if not users:
                errors.append("Email not in database. Please register.")
            else:
                user = users[0]
                if not bcrypt.checkpw(password.encode(), user.password.encode()):
                    errors.append("Password does not match password in database.")
        if not password:
            errors.append("Password is required.")

        if not errors:
            user = User.objects.get(email = email)
            return (True, user)
        else:
            return (False, errors)


class ProductManager(models.Manager):

    def productValidator(self, form, id):

        errors = []

        name = form['name']
        price = form['price']

        if not name:
            errors.append("Product name is required.")
        elif len(name) < 3:
            errors.append("Product name must be at least 3 characters.")
        if not price:
            errors.append("price is required.")
        elif not price.isnumeric():
            errors.append("Must be valid price.")

        if not errors:
            # save user in database
            product = Product.objects.create(name=name, price=price, seller_id=id)
            return (True, product)
        else:
            return (False, errors)


class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __repr__(self):
        return "<User: {} {}>".format(self.fname, self.lname)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    seller = models.ForeignKey(User, related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = ProductManager()
    # sold joins in transaction

    def __repr__(self):
        return "<Product: {}>".format(self.name)

class Transaction(models.Model):
    sale = models.ForeignKey(Product, related_name="sold")
    buyer = models.ForeignKey(User, related_name="bought")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



