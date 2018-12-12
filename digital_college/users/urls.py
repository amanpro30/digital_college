from django.urls import path, include
from users import views as user_views

app_name = 'users'

urlpatterns = [
    path('User_Home/', include('after_login.urls')),
    path('College_Home', user_views.College_Home, name='College_Home'),
    path('User_Registration/', user_views.User_Registration, name='User_Registration'),
    path('College_Registration/', user_views.College_Registration, name='College_Registration'),
    path('activate/<uidb64>/<token>/', user_views.activate, name='activate'),
    path('add_courses/', user_views.add_courses, name='add_courses'),
    path('reset/', user_views.PasswordReset, name='reset'),
    path('reset/<uidb64>/<token>/', user_views.reset2, name='reset'),
    path('edit/', user_views.profile_update, name='edit'),
    path('edit2/', user_views.profile_update2, name='edit2'),
]

