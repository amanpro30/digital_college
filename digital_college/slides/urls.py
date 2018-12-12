from django.urls import path, include
from slides import views

app_name = "slides"

urlpatterns = [
    path('download/<id>/', views.download, name='download'),
    path('addSlides/', views.addAssign, name='add'),
    path('delete/<int:file_id>', views.delAssign, name='delete'),
]
