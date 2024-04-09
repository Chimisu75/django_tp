from django.shortcuts import render, redirect
from .models import tabTrains
from .forms import TrainForm
# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def regulation(request):
    print("la vue est apellée")
    return render(request, 'regulation.html', {})

def liste_departs(request):
    departs = tabTrains.objects.all()
    return render(request, 'regulation.html', {'departs': departs})

def add_train(request):
    if request.method == 'POST':
        form = TrainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('regulation')  
    else:
        form = TrainForm()
    return render(request, 'train_form.html', {'form': form})

def recherche_train(request):
    query = request.GET.get('query', '')
    if query:
        # Filtrez les trains en fonction de la requête
        trains = tabTrains.objects.filter(destination__icontains=query) | tabTrains.objects.filter(train_id__icontains=query)
    else:
        trains = tabTrains.objects.all()
    return render(request, 'recherche_train.html', {'trains': trains})
