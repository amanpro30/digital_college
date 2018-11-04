from django.urls import path
from . import views

app_name = "clubs"

urlpatterns = [
    path('', views.home, name='forum'),
    path('contacts/', views.contacts, name='contacts'),
    path('gallery/', views.gallery, name='gallery'),
    path('post/', views.post, name="post"),
]
