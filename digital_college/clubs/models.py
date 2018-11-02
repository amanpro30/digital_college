from django.db import models
from users.models import Registered_User


class Post(models.Model):
    UserId = models.ForeignKey(Registered_User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    subject = models.CharField(max_length=500)
    content = models.TextField()
