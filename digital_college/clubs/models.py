from django.db import models
from users.models import Registered_User
from django.utils import timezone


class Post(models.Model):
    UserId = models.ForeignKey(Registered_User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=timezone.now)
    subject = models.CharField(max_length=500)
    content = models.TextField(default='')

    def __str__(self):
        return self.subject


class Images(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    image = models.ImageField(blank=True, null=True, upload_to='profile_pics')

    def __str__(self):
        post = Post.objects.get(pk=self.postId)
        return post
