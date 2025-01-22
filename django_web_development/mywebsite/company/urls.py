from django.urls import path
from .views import * # .view the dot indicate relative path(same folder with this file)

urlpatterns = [
    path('', home, name='home-page'), # localhost:8000/
    path('about/', about_us, name='about-page'), # localhost:8000/about/
    path('contact/', contact_us, name='contact-page'),
    path('accountant/', accountant, name='account-page'),
]