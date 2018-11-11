from django.urls import path, include
# from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('User_Home/', user_views.User_Home, name='User_Home'),
    path('College_Home', user_views.College_Home, name='College_Home'),
    path('User_Registration/', user_views.User_Registration, name='User_Registration'),
    path('College_Registration/', user_views.College_Registration, name='College_Registration'),
    path('classroom/', user_views.after_login, name='after_login'),
    path('progress_report/', user_views.progress_report, name='progress_report'),
    path('calender/', user_views.calender, name='calender'),
    path('profile/', user_views.profile, name='profile'),
]
