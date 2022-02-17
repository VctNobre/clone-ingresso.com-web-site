from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('filmes', views.filmes, name='filmes'),
    path('cinemas', views.cinemas, name='cinemas')
] 
