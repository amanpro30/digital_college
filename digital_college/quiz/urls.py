from django.urls import path, include
from . import views as views

app_name = 'quiz'

urlpatterns = [
    path('quiz_home/', views.quiz_home, name='quiz_home'),
    path('quiz_home/<str:quiz_name>', views.take_quiz, name='take_quiz'),
    path('create_quiz/', views.create_quiz, name='create_quiz'),
    path('quiz_home/<str:quiz_name>/result', views.quiz_result, name='quiz_result'),
    path('quiz_api/', include('quiz.api.urls', namespace='api')),
]
