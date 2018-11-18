from django.urls import path, include
from slides import views

urlpatterns = [
    path('download/Assignment/<id>/', views.download, name='download'),
    path('addSlides/',views.addAssign,name='add'),
    path('delete/<str:file_id>',views.delAssign,name='delete'),
]