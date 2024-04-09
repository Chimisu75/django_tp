from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('regulation/', views.liste_departs, name='regulation'),
    path('add/', views.add_train, name='add_train'),
    path('recherche/', views.recherche_train, name='recherche_train'), 
]
