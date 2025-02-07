from django.urls import path, re_path
from django.shortcuts import redirect
from .views import classify_number, home

def redirect_to_correct_url(request):
    """Redirects invalid root requests to the correct API endpoint."""
    number_param = request.GET.get("number")
    if number_param:
        return redirect(f"/api/classify-number/?number={number_param}")
    return home(request)

urlpatterns = [
    re_path(r'^$', redirect_to_correct_url, name="redirect_to_correct_url"),
    path('api/classify-number/', classify_number, name="classify_number"),
]
