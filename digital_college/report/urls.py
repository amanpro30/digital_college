from django.urls import path, include
from . import views

app_name='report'

urlpatterns = [
    path('test/',views.test,name='test'),
]