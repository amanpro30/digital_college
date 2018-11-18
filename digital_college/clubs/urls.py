from django.urls import path
from . import views
from after_login import views as login_view

app_name = "clubs"

urlpatterns = [
    path('', login_view.clubs, name='cl_list'),
    path('', views.home, name='forum'),
    path('contacts/', views.contacts, name='contacts'),
    path('gallery/', views.gallery, name='gallery'),
    path('post/', views.post, name='post'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('dislike/<int:post_id>/', views.dislike_post, name='dislike_post'),
    path('comment/<int:post_id>/', views.comment, name="comment")
]
