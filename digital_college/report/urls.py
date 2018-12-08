from django.urls import include, path
from . import views

app_name = 'report'

urlpatterns = [
    path('test/', views.test, name='report'),
    path('test1/', views.test1, name='report'),
    #path('exam_result/<str:file_name>', name='report'),

]
