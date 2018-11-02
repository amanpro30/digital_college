from django.urls import path
from . import views

app_name = "clubs"

urlpatterns = [
    path('', views.home, name='home'),
    path('forum/', views.forum, name='forum'),
    path('contacts/', views.contacts, name='contacts'),
    path('post/', views.post, name='post'),
    path('gallery/', views.gallery, name='gallery'),
]
