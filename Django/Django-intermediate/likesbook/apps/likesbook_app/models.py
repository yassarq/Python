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
        elif len(fname) < 2:
            errors.append("First name must be at least 2 characters.")
        elif not fname.isalpha():
            errors.append("First name cannot contain numbers.")
        if not lname:
            errors.append("Last name is required.")
        elif len(lname) < 2:
            errors.append("Last name must be at least 2 characters.")
        elif not lname.isalpha():
            errors.append("Last name cannot contain numbers.")
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


        # print(errors)

        if not errors:
            # get user from database
            user = User.objects.get(email = email)
            return (True, user)
        else:
            return (False, errors)

class BookManager(models.Manager):
    def bookValidator(self, form, id):

        errors = []

        bookname = form['bookname']
        description = form['description']

        
        if not bookname:
            errors.append("Book name is required.")
        if not description:
            errors.append("Description is required.")
        if not errors:
            # save user in database
            errors.append("Successfully Added a Book")
            book = Book.objects.create(bookname = bookname, description = description, uploaded_by_id = id)
            return (True, book, errors)
        else:
            return (False, errors)

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # uploadedbooks -> joins to Book table (uploaded_by)
    # likedbooks -> joins to Book table (readers)

    objects = UserManager()

    def __repr__(self):
        return "<User: {} {}>".format(self.fname, self.lname)


class Book(models.Model):
    bookname = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name="uploadedbooks")
    readers = models.ManyToManyField(User, related_name="likedbooks")

    objects = BookManager()

    def __repr__(self):
        return "<Book: {}>".format(self.bookname)