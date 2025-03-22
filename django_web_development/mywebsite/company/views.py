from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# from django.contrib.auth.views import LogoutView


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


def login(request):
     context = {}

     if request.method == 'POST':
        data = request.POST.copy() # data return a dict
        username = data.get('username')
        password = data.get('password')
        try:
             user = authenticate(username=username, password=password)
             login(request, user)
        except:
             context['message'] = 'username หรือ password ไม่ถูกต้อง'

     return render(request, 'company/login.html', context)

# class CustomLogoutView(LogoutView):
#     template_name = 'company/logout.html'  # Specify your template here

def accountant(request):
     all_contact = ContactList.objects.all()
    #  all_contact = ContactList.objects.all().order_by('-id'); .order_by('-id') reverse the order of all_contact list เอา contact ล่าสุดอยู่ข้างบน
     context = {'all_contact': all_contact}
     return render(request, 'company/accountant.html', context)

def register(request):
     context = {}

     if request.method == 'POST':
        data = request.POST.copy() # data return a dict
        fullname = data.get('fullname')
        tel = data.get('telephone')
        username = data.get('username')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        # check user ว่ามีในระบบรึยัง
        try:
             check = User.objects.get(username=username)
            #  context['warning'] = f'email: {username} มีในระบบเเล้ว กรุณาใช้ email อื่น'
            #  return render(request, 'company/register.html', context)
        except:
            if password != confirm_password:
                context['warning'] = 'กรุณากรอกรหัสผ่านให้ถูกต้องทั้งสองช่อง'
                return render(request, 'company/register.html', context)

            new_user = User()
            new_user.username = username
            new_user.email = username
            new_user.first_name = fullname
            new_user.set_password(password)
            new_user.save()

            new_profile = Profile()
            new_profile.user = User.objects.get(username=username)
            new_profile.tel = tel
            new_profile.save()
        # try:
        #      user = authenticate(username=username, password=password)
        #      login(request, user)
        # except:
        #      context['message'] = 'username หรือ password ไม่ถูกต้อง'

     return render(request, 'company/register.html', context)