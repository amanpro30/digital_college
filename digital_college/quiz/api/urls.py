from django.urls import path, include
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.QuizView.as_view(), name="api_get"),
]

