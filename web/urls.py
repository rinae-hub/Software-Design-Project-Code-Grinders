from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import messages
from .import views

urlpatterns = [
    path('abc/', views.abc, name='abc'),
    path('',views.home_view, name='home'),
    path('home/', views.redirect_view),
    path('register/', views.register_view, name='register')
]

