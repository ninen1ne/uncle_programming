from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product) # allow admin see database
admin.site.register(ContactList)
admin.site.register(Profile)
