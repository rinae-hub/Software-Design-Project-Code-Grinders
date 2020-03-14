from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='DESKTOP-home'),
    path('login/',views.login,name='DESKTOP-login')
]
