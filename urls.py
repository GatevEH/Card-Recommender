from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cardsRecommender/<int:id>/', views.card, name='card'),
]