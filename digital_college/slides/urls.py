from django.urls import path, include
from slides import views

app_name = "slides"

urlpatterns = [
    path('download/<id>/', views.download, name='download'),
    path('addSlides/', views.addSlides, name='addSlides'),
    path('delete/<str:file_id>', views.delSlides, name='delete'),
    path('addAssign/',views.addAssign,name='addAssign'),
]
