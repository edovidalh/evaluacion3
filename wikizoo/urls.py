from django import urls
from django.urls import path

from .views import animal, main

urlpatterns = [
    path('', main, name="Main"),
    path('Animal', animal, name="Animal")
]

