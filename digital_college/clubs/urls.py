from django.urls import path
from . import views
from after_login import views as login_view

app_name = "clubs"

urlpatterns = [
    path('', login_view.clubs, name='cl_list'),
    path('<str:club_name>/', views.post, name='forum'),
    path('<str:club_name>/postmob', views.post_mob, name='post_mob'),
    path('<str:club_name>/contacts/', views.contacts, name='contacts'),
    path('<str:club_name>/gallery/', views.gallery, name='gallery'),
    path('<str:club_name>/post/', views.post, name='post'),
    path('<str:club_name>/delete/<int:post_id>/', views.delete, name='delete'),
    path('<str:club_name>/update/<int:post_id>/', views.update, name='update'),
    path('<str:club_name>/like/<int:post_id>/', views.like_post, name='like_post'),
    path('<str:club_name>/dislike/<int:post_id>/', views.dislike_post, name='dislike_post'),
    path('<str:club_name>/comment/<int:post_id>/', views.comment, name="comment"),
    path('<str:club_name>/delcom/<int:com_id>/', views.delcom, name="delcom"),
    path('<str:club_name>/postDetail/<int:post_id>/', views.postdetail, name="postdetails"),
    path('<str:club_name>/reply/<int:com_id>/', views.reply, name="reply"),
    path('<str:club_name>/delrep/<int:rep_id>/', views.delrep, name="delrep"),
]
