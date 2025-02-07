from django.urls import path
from .views import classify_number, home

urlpatterns = [
    path('', home, name="home"),
    path('classify-number', classify_number, name="classify_number"),
]
