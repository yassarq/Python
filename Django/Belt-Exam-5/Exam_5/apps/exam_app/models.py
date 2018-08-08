from django.db import models
import re
import bcrypt
from datetime import datetime

class UserManager(models.Manager):
    def register(self, name, alias, email, password, password_confirmation, date):
    errors = {}
    now = str(datetime.now())
        if (len(name) < 3):
            errors['name'] = "Name needs to be at least two letters long"

        if (len(alias) < 3):
            errors['alias'] = "Alias needs to be at least two letters long"

        if (len(password) < 8):
            errors['password'] = "Password needs to be at least eight characters long"

        if (password != password_confirmation):
            errors['password'] = "Passwords do not match"
        try:
            existingUser = self.get(email__iexact=email)
        except:
            existingUser = None
        if (existingUser):
            errors['email'] = 'That email is already registered'

        if (not EMAIL_REGEX.match(email)):
            errors['email'] = 'Invalid email.'

        if (not date:
            errors.append("Date is required.")
        elif date > now:
            errors.append("Date can't be in the future")

        if (date > now):
            error['date'] = 'Please select a date'

        if (errors):
            return (False, errors)
        else:
            password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            self.create(email=email, name=name, alias=alias, password=password, birthday=birthday)

            return (True, self.get(email=email))
        

        if not errors:
            # save user in database
            hash_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = User.objects.create(name=name, username=username, password=hash_pw)
            return (True, user)
        else:
            return (False, errors)


    def login(self, email, password):
        try:
            user = self.get(email__iexact=email)
        except:
            user = None
        if user and bcrypt.hashpw(password.encode('utf-8'), user.password.encode('utf-8')) == user.password.encode('utf-8'):
            return (True, user)

        return(False, "login failed")

class PokeManager(models.Manager):
    def Poke(self, form, uId):
        try:
            userToPoke = User.objects.get(id=id)
            loggedUser - User.objects.get(id=uId)
            Poke.onjects.create(poker=loggedUser, pokie=userToPoke)
        except :
            print
        errors = []
        poke = form['pokergotten']

        if not poke:
            poke = poke[0]

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    joins = models.ManyToManyField('self', related_name='combined+')
    objects = UserManager()

    # def __repr__(self):
    #     return "<User: {} id:{}>".format(self.name, self.)

class Poke(models.Model):
    send_user = models.ForeignKey(User, related_name="poker")
    receive_user = models.ForeignKey(User, related_name="pokee")
    poke_date = models.DateTimeField('date poked')

    def __unicode__(self):
    return "Poke from {0} to {1}".format(self.send_user.username, self.receive_user.username)

    # Really just for fun since we can
    def was_poked_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.poke_date <= now

    was_poked_recently.admin_order_field = 'poke_date'
    was_poked_recently.boolean = True
    was_poked_recently.short_description = 'Poked recently?'
