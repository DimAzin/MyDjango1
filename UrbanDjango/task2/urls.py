# task2/urls.py
from django.urls import path
from .views import class_based_view, function_based_view

print("Loading task2 URLs...")

urlpatterns = [
    path('class/', class_based_view, name='class_based'),
    path('function/', function_based_view, name='function_based'),
]



