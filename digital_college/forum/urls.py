from django.urls import path
from . import views

app_name = "class_forum"

urlpatterns = [
    path('', views.forum, name="cl_forum"),
]
