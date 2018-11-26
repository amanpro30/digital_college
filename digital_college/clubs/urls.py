from django.urls import path
from . import views
from after_login import views as login_view

app_name = "clubs"

urlpatterns = [
    path('', login_view.clubs, name='cl_list'),
    path('cl/', views.home, name='forum'),
    path('cl/contacts/', views.contacts, name='contacts'),
    path('cl/gallery/', views.gallery, name='gallery'),
    path('cl/post/', views.post, name='post'),
    path('cl/delete/<int:post_id>/', views.delete, name='delete'),
    path('cl/update/', views.update, name='update'),
    path('cl/like/<int:post_id>/', views.like_post, name='like_post'),
    path('cl/dislike/<int:post_id>/', views.dislike_post, name='dislike_post'),
    path('cl/comment/<int:post_id>/', views.comment, name="comment")
]
