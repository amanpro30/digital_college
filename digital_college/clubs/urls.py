from django.urls import path
from . import views

app_name = "clubs"

urlpatterns = [
    path('', views.home, name='forum'),
    path('contacts/', views.contacts, name='contacts'),
    path('gallery/', views.gallery, name='gallery'),
    path('post/', views.post, name="post"),
    path('classroom/', views.after_login, name='after_login'),
    path('progress_report/', views.progress_report, name='after_login'),
    path('planner/', views.planner, name='after_login'),
    path('profile/', views.profile, name='after_login'),
]
