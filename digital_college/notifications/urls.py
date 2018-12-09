from django.urls import path
from . import views

app_name='notifications'

urlpatterns=[
    path('',views.show_notifications,name='show_notifications'),
    path('<int:notification_id>/delete',views.delete_notifications,name='delete_notifications')
]