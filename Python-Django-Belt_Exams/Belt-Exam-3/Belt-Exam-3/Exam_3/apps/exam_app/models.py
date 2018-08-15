from django.db import models
import re
import bcrypt
from datetime import datetime

class UserManager(models.Manager):

    def regValidator(self, form):

        errors = []

        name = form['name']
        username = form['username'].lower()
        password = form['password']
        confirm_pw = form['confirm_pw']
        date = form['date_hired']
        now = str(datetime.now())

        if not name:
            errors.append("Name is required.")
        elif len(name) < 3:
            errors.append("Name must be at least 3 characters.")
        elif not name.isalpha():
            errors.append("Name cannot contain numbers.")
        if not username:
            errors.append("Username is required.")
        elif len(username) < 3:
            errors.append("Username must be at least 3 characters.")
        else:
            users = User.objects.filter(username = username)
            if users:
                errors.append("Username already exists. Please login.")
        if not password:
            errors.append("Password is required.")
        elif len(password) < 8:
            errors.append("Password must have at least 8 characters.")
        if not confirm_pw:
            errors.append("Confirm password is required.")
        if password != confirm_pw:
            errors.append("Passwords must match.")
        if not date:
            errors.append("Date is required.")
        elif date > now:
            errors.append("Date can't be in the future")
        

        if not errors:
            # save user in database
            hash_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = User.objects.create(name=name, username=username, password=hash_pw)
            return (True, user)
        else:
            return (False, errors)


    def loginValidator(self, form):
        errors = []

        username = form['username'].lower()
        password = form['password']

        if not username:
            errors.append("Username is required.")
        else:
            users = User.objects.filter(username = username)
            if not users:
                errors.append("Username not in database. Please register.")
            else:
                user = users[0]
                if not bcrypt.checkpw(password.encode(), user.password.encode()):
                    errors.append("Password does not match password in database.")
        if not password:
            errors.append("Password is required.")

        if not errors:
            user = User.objects.get(username = username)
            return (True, user)
        else:
            return (False, errors)

class QuoteManager(models.Manager):
    def quoteValidator(self, form, id):
        errors = []
        quote_by = form["quote_by"]
        message = form["message"]

        if not quote_by:
            errors.append("Name is required.")
        if not message:
            errors.append("Message is required.")
        if not errors:
            list = List.objects.create(author = quote_by, poster_id = id, quote = message)
            return (True, list)
        else:
            return (False, errors)

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    joins = models.ManyToManyField('self', related_name='combined+')
    objects = UserManager()
    # Added list (-> List)

    def __repr__(self):
        return "<User: {} id:{}>".format(self.name, self.id)

class List(models.Model):
    quote = models.CharField(max_length=255)
    poster = models.ForeignKey(User,related_name="my_quotes")
    author = models.CharField(max_length=255)
    favorites = models.ManyToManyField(User, related_name="my_faves")
    objects = QuoteManager()

    def __repr__(self):
        return "<List: {} id:{}>".format(self.quote, self.id)