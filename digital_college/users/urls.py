from django.urls import path,include
from users import views as user_views
from django.contrib.auth import views as auth_views
from after_login import views as login_views


app_name='users'

urlpatterns = [
    path('User_Home/', login_views.after_login, name='User_Home'),
    path('College_Home', user_views.College_Home, name='College_Home'),
    path('User_Registration/', user_views.User_Registration, name='User_Registration'),
    path('College_Registration/', user_views.College_Registration, name='College_Registration'),
    path('activate/<uidb64>/<token>/', user_views.activate, name='activate'),
]
