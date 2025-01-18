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

def contact_us(request):

    context = {} # thing that you want to attach to
    if request.method == 'POST':
        data = request.POST.copy()
        title = data.get('title')
        email = data.get('email')
        detail = data.get('detail')
        print(f'{title}\n{email}\n{detail}')
        print('-------------')

        # ถ้า user ไม่กรอกข้อมูล
        if title == '' or email=='':
                context['message'] = 'Please fill the Contact topic and Email.'
                return render(request, 'company/contact.html', context)

        # when receive data stored this data
        # Contactlist(title=title, email=email, detail=detail).save()
        new_record = ContactList()
        new_record.title = title
        new_record.email = email
        new_record.detail = detail
        new_record.save()
        context['message'] = 'We have received your contact information.'

    return render(request, 'company/contact.html', context)