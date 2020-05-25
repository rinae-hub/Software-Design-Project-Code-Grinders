from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import messages
from .import views

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('abc/logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('abc/', views.abc, name='abc'),
    path('',views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
]
