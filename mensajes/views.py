from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate

# Create your views here.
