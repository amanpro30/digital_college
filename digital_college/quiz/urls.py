from django.urls import path
from . import views as views


urlpatterns = [
    path('quiz_home/',views.quiz_home),
    path('quiz_home/<str:quiz_name>',views.take_quiz,name='take_quiz'),
    path('create_quiz/',views.create_quiz,name=''),
    path('quiz_home/<str:quiz_name>/result',views.quiz_result,name='quiz_result')
]