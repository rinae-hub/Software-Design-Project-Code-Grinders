from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})  # templates


def log_view(request, *args, **kwargs):
    return render(request, "log.html", {})


def base_view(request, *args, **kwargs):
    return render(request, "base.html", {})


def team_view(request, *args, **kwargs):
    return render(request, "team.html", {})


def mentors_view(request, *args, **kwargs):
    return render(request, "mentors.html", {})
