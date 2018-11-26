from django.urls import path
from . import views
from after_login import views as login_view

app_name = "clubs"

urlpatterns = [
    path('', login_view.clubs, name='cl_list'),
    path('<str:club_name>/', views.home, name='forum'),
    path('<str:club_name>/contacts/', views.contacts, name='contacts'),
    path('<str:club_name>/gallery/', views.gallery, name='gallery'),
    path('<str:club_name>/post/', views.post, name='post'),
    path('<str:club_name>/delete/<int:post_id>/', views.delete, name='delete'),
    path('<str:club_name>/update/', views.update, name='update'),
    path('<str:club_name>/like/<int:post_id>/', views.like_post, name='like_post'),
    path('<str:club_name>/dislike/<int:post_id>/', views.dislike_post, name='dislike_post'),
    path('<str:club_name>/comment/<int:post_id>/', views.comment, name="comment")
]
