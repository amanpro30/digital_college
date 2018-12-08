from django.urls import path
from . import views

app_name = "class_forum"

urlpatterns = [
    path('', views.forum, name="cl_forum"),
    path('delete/<int:post_id>/', views.delete, name="cl_delete"),
    path('comment/<int:post_id>/', views.comment, name="cl_comment"),
    path('details/<int:post_id>/', views.postdetails, name="cl_post"),
    path('delcom/<int:com_id>/', views.delcom, name="cl_delcom"),
    path('dislike/<int:post_id>/', views.dislike_post, name="cl_dislike"),
    path('like/<int:post_id>/', views.like_post, name="cl_like"),
    path('reply/<int:com_id>/', views.reply, name="cl_reply"),
    path('delreply/<int:rep_id>/', views.delreply, name="cl_delreply"),
    path('update/<int:post_id>/', views.update, name="cl_updatepost"),
]
