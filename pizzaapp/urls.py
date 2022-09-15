from django.urls import path
from django.conf import settings

from pizzaapp.views import home, add

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('add/', add, name='add'),
]