from django.db import models
import re
import bcrypt
from datetime import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):

    def regValidator(self, form):

        errors = []

        name = form['name']
        username = form['username'].lower()
        email = form['email']
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
            user = User.objects.create(name=name, username=username, email=email, password=hash_pw)
            return (True, user)
        else:
            return (False, errors)


    def loginValidator(self, form):
        errors = []

        email = form['email'].lower()
        password = form['password']

        if not email:
            errors.append("Email is required.")
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


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    joins = models.ManyToManyField('self', related_name='combined+')
    objects = UserManager()
    # Added list (-> List)

    # def __repr__(self):
    #     return "<User: {} id:{}>".format(self.name, self.)



