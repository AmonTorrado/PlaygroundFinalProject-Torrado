from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2=forms.CharField(label="Repita la contraseña", widget = forms.PasswordInput)