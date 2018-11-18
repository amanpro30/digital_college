from django.urls import path, include
from . import views
from after_login import views as login_view

app_name = 'classroom'

urlpatterns = [
    path('', login_view.after_login, name='after_login'),
    path('<str:class_name>/', views.class_home, name='class_home'),
    path('<str:class_name>/quiz/', include('quiz.urls')),
    # path('<str:class_name>/assignment',include('assignment.urls')),
    # path('<str:class_name>/slide',include('slide.urls')),
    # path('<str:class_name>/report',include('report.urls')),
]
