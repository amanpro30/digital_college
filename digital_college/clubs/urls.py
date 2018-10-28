from django.urls import path
from . import views

urlpatterns = [
    path('', views.clubs, name='clubs_forum'),
]
