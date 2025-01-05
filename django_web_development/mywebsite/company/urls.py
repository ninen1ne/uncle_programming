from django.urls import path
from .views import home # .view the dot indicate relative path(same folder with this file)

urlpatterns = [
    path('', home),
]