from django.urls import path
from . import views as classroom_views

urlpatterns = [
    path('quiz',classroom_views.quiz),
    path('assignment',classroom_views.assignment),
    path('slides',classroom_views.slides),
    path('forum',classroom_views.forum),
    path('result',classroom_views.result,name='result')
]