from django.urls import path
from . import views

urlpatterns = [
    path('', views.player_club_stint, name = 'player_club_stint')
]