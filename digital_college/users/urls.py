from django.urls import path,include
#from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('User_Home/', user_views.User_Home, name='User_Home'),
    path('College_Home', user_views.College_Home, name='College_Home'),
    path('User_Registration/', user_views.User_Registration, name='User_Registration'),
    path('College_Registration/', user_views.College_Registration, name='College_Registration'),
]