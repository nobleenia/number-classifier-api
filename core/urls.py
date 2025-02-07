from django.urls import path
from .views import classify_number, home

urlpatterns = [
    path('', home),
    path('api/classify-number', classify_number),
]
