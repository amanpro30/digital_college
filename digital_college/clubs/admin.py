from django.contrib import admin
from .models import Post, Images, Comment, Reply, Like

# Register your models here.
admin.site.register(Post)
admin.site.register(Images)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Like)
