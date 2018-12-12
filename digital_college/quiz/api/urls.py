from django.urls import path, include
from . import views

app_name = 'api'

urlpatterns = [
    path('<int:quiz_id>/', views.QuizView.as_view(), name="api_get"),
]

