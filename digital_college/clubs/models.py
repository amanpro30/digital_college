from django.db import models
from users.models import Registered_User, Clubs, Registered_College
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    clubId = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    collegeId = models.ForeignKey(Registered_College, on_delete=models.CASCADE)
    userId = models.ForeignKey(Registered_User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=timezone.now)
    subject = models.CharField(max_length=500)
    content = models.TextField(default='')

    def __str__(self):
        return self.subject


class Images(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='')

    def __str__(self):
        return self.postId.subject


class Comment(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    userId = models.ForeignKey(Registered_User, on_delete=models.DO_NOTHING)
    comment = models.TextField(default='')

    def __str__(self):
        com = self.comment[:10] + "..."
        return com


class Reply(models.Model):
    comId = models.ForeignKey(Comment, on_delete=models.CASCADE)
    userId = models.ForeignKey(Registered_User, on_delete=models.DO_NOTHING)
    reply = models.TextField(default='')

    def __str__(self):
        rep = self.reply[:10] + "..."
        return rep


class Like(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    userId = models.ForeignKey(Registered_User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["postId", "userId"]

    def __str__(self):
        return self.userId.user.username


class ClubSlideShowInfo(models.Model):
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    image = models.ImageField()
    heading = models.CharField(max_length=40, blank=True)
    caption = models.CharField(max_length=100, blank=True)