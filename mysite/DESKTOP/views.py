from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render(request, 'DESKTOP/home.html')
#render can take a third variable  'context' check it on video part 3

#
def login(request):
    return render(request,'DESKTOP/login.html')
