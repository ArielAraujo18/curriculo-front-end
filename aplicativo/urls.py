# aplicativo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Define a URL principal para renderizar a view home
]