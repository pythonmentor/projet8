from django.urls import path, reverse
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('article/<int:id>', views.lire, name='lire'),
    path('search/', views.search, name='search')

]