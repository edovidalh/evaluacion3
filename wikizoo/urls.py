from django import urls
from django.urls import path

from .views import animal, informacion, main

urlpatterns = [
    path('', main, name="Main"),
    path('Animal', animal, name="Animal"),
    path('Informacion', informacion, name="Informacion"),
    path('Main', main, name="Main"),
    
]

