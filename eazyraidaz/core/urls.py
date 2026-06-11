from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('join/', views.join, name='join'),
    path('join/success/', views.join_success, name='join_success'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]
