from django.urls import path, include
from . import views
from after_login import views as login_view

app_name = 'classroom'

app_name1 = '1classroom'

urlpatterns = [
    path('', login_view.after_login, name='after_login'),
    path('<str:class_name>/', views.class_home, name='class_home'),
    path('<str:class_name>/quiz/', include('quiz.urls', namespace='quiz')),
    # path('<str:class_name>/assignment',include('assignment.urls')),
    path('<str:class_name>/slides/', include('slides.urls', namespace='slides')),
    path('<str:class_name>/report/', include('report.urls', namespace='report')),
    path('<str:class_name>/forum/', include('forum.urls', namespace='class_forum')),
    path('<str:class_name>/members/', views.members, name="members"),
    path('<str:class_name>/members/delstud/<int:user_id>/', views.remStudent, name="remStud"),
    path('<str:class_name>/members/addstudent/', views.addStudents, name="addStud"),
    path('<str:class_name>/members/addstudent/<int:stud_id>', views.addStud, name="add"),
    # path('<str:class_name>/report',include('report.urls')),
]
