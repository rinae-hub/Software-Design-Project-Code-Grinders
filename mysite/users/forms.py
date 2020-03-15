from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    student_Number=forms.CharField(required=True)

    class Meta:
        model= User
        fields= ['username','email','student_Number','password1','password2']
