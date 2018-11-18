from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from users.models import Registered_User


class Entry(models.Model):
    userId = models.ForeignKey(Registered_User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
