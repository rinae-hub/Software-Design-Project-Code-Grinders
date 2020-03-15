from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home,name='DESKTOP-home'),
    path('login/',views.login,name='DESKTOP-login')

]
