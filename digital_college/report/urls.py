from django.urls import include, path
from . import views

app_name = 'report'

urlpatterns = [
    path('test/', views.student_graph, name='student_graph'),
    path('test1/', views.faculty_graph, name='faculty_graph'),
]
