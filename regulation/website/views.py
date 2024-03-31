from django.shortcuts import render
from .models import tabTrains

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def regulation(request):
    print("la vue est apellée")
    return render(request, 'regulation.html', {})

def liste_departs(request):
    departs = tabTrains.objects.all()
    return render(request, 'regulation.html', {'departs': departs})