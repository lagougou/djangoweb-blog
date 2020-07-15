from django.urls import path
from .views import *

urlpatterns = [
    path('register.html', register, name='register'),
    path('lgoin.html', userLogin, name='userLogin'),
    path('about/<int:id>.html', about, name='about'),
]