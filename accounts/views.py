from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm


# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login1')
    else:

        form = UserRegisterForm()
    return render(request, 'accounts/register1.html', {'form': form})
