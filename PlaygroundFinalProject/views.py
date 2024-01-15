from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def inicio (request):
    return render(request, "inicio.html")

def about (request):
    return render(request, "about.html")