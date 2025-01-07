from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def home(request):
#     return HttpResponse('<h1>Hello World!</h1> <br> <p>By Norawee Yolle</p>')

def home(request):
    return render(request, 'company/home.html')
    #'DIRS': [BASE_DIR / 'company/template'], + 'company/home.html' (base_dir is location where a project are stored)