from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def regValidator(self, form):

        errors = []

        name = form['name']
        alias = form['alias']
        email = form['email'].lower()
        password = form['password']
        confirm_pw = form['confirm_pw']

        if not name:
            errors.append("Name is required.")
        elif len(name) < 2:
            errors.append("Name must be at least 2 characters.")
        elif not name.isalpha():
            errors.append("Name cannot contain numbers.")
        if not alias:
            errors.append("Alias is required.")
        elif len(alias) < 2:
            errors.append("Alias must be at least 2 characters.")
        elif not alias.isalpha():
            errors.append("Alias cannot contain numbers.")
        if not email:
            errors.append("Email is required.")
        elif not EMAIL_REGEX.match(email):
            errors.append("Invalid Email")
        else:
            users = User.objects.filter(email = email)
            if users:
                errors.append("Email already exists. Please Log in.")
        if not password:
            errors.append("Password is required.")
        if not confirm_pw:
            errors.append("Confirm password is required.")
        if password != confirm_pw:
            errors.append("Passwords must match.")

        if not errors:
            # save user in database
            hash_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = User.objects.create(name=name, alias=alias, email=email, password=hash_pw)
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


        # print(errors)

        if not errors:
            # get user from database
            user = User.objects.get(email = email)
            return (True, user)
        else:
            return (False, errors)

class ProductManager(models.Manager):
    def productValidator(self, form, id):

        errors = []

        productname = form['productname']

        
        if not productname:
            errors.append("Product name is required.")
        if not errors:
            # save user in database
            errors.append("Successfully Added a Product")
            product = Product.objects.create(productname = productname, uploaded_by = User.objects.get(id=id))
            return (True, product, errors)
        else:
            return (False, errors)

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # uploadedproduct -> joins to Product table (uploaded_by)
    # likedproduct -> joins to Product table (likers)

    objects = UserManager()

    def __repr__(self):
        return "<User: {} {}>".format(self.name, self.alias)

class Product(models.Model):
    productname = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name="uploadedproduct")
    likers = models.ManyToManyField(User, related_name="likedproduct")

    objects = ProductManager()

    def __repr__(self):
        return "<Product: {}>".format(self.productname)