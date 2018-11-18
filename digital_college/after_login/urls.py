from django.urls import path, include
from . import views

app_name = "after"

urlpatterns = [
    path('', views.after_login, name='after_login'),
    path('classroom/', include('classrooms.urls', namespace='classroom')),
    path('progress_report/', views.progress_report, name='progress_report'),
    path('calendar/', include('calendarapp.urls', namespace='calendarapp')),
    path('profile/', views.profile, name='profile'),
    path('faculty/', views.faculty, name='faculty'),
    path('clubs/', include('clubs.urls', namespace='clubs')),
    path('students/', views.students, name="students"),
]
