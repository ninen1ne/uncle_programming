from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

# def home(request):
#     return HttpResponse('<h1>Hello World!</h1> <br> <p>By Norawee Yolle</p>')

def home(request):
    all_product = Product.objects.all()
    context = {'all_product': all_product} # SELECT * from product
    return render(request, 'company/home.html', context)
    #'DIRS': [BASE_DIR / 'company/template'], + 'company/home.html' (base_dir is location where a project are stored)

def about_us(request):
    return render(request, 'company/about_us.html')