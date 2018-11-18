from django.urls import path, include
from . import views

urlpatterns = [
    path('download/Assignment/<id>/', views.download, name='download'),
    path('addAssign/',views.addAssign,name='add'),
    path('delete/<str:file_id>',views.delAssign,name='delete'),
]