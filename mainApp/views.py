from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. Index should eventually pass to the dashboard controller.")

def dashboard(request):
    return HttpResponse("This is the dashboard screen.")
