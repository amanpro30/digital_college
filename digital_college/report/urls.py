<<<<<<< HEAD
from django.urls import path, include
from . import views

app_name='report'

urlpatterns = [
    path('test/',views.test,name='test'),
]
=======
from django.urls import include, path
from . import views

app_name = 'report'

urlpatterns = [
    path('test/', views.student_graph, name='student_graph'),
    path('test1/', views.faculty_graph, name='faculty_graph'),
]
>>>>>>> 14f158157c979a2936952e3b943b3a4495be888c
