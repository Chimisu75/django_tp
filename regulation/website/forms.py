from django import forms
from .models import tabTrains

class  TrainForm(forms.ModelForm):
    class Meta:
        model = tabTrains
        fields= ['train_id', 'heure_depart', 'destination', 'voie']