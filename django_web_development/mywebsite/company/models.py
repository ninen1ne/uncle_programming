from django.db import models
from django.contrib.auth.models import User
# Create your models here.(database)

"""
Product(name of table)
    - title (Char)
    - description (Text)
    - price (Decimal)
    - quantity (Int)
"""

"""
After create or change models run 2 commands from terminal:
1) python manage.py makemigrations
2) python manage.py migrate
"""

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True, default=1)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class ContactList(models.Model):
    title = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    detail = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    # this func allow admin site see title of this model.
    # if not use this func you will get return obj not title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=100, default='member') # user role
    point = models.IntegerField(default=0)
    tel = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username
