from django.db import models

# Create your models here.

class tabTrains(models.Model):
    train_id = models.CharField(max_length=10)
    heure_depart = models.TimeField()
    destination = models.CharField(max_length= 50)
    voie = models.CharField(max_length=10)