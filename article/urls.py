from django.urls import path
from django.views.generic import RedirectView
from .views import *

urlpatterns = [
    path('', RedirectView.as_view('user/login.html')),
    path('<int:id>/<int:page>.html', article, name='article'),
    path(),
]