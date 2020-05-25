from django.contrib import messages
from django.shortcuts import render
import requests
from subprocess import run, PIPE
import sys
from django.shortcuts import render, redirect
from .forms import UserRegisterForm


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})  # templates


def abc(request, *args, **kwargs):
    return render(request, "abc.html", {})  # templates


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:

        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def redirect_view(request):
    response = redirect('home/')
    return response

