from django.urls import path
from . import views

app_name = "after"

urlpatterns = [
    path('classroom/', views.after_login, name='after_login'),
    path('progress_report/', views.progress_report, name='progress_report'),
    path('calender/', views.calender, name='calender'),
    path('profile/', views.profile, name='profile'),
]


