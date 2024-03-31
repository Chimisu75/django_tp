from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('regulation/', views.liste_departs, name='regulation'),
]
