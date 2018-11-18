from django.db import models
from users.models import Registered_User


class Faculty(models.Model):
    faculty = models.ForeignKey(Registered_User, on_delete=models.CASCADE)
    descript = models.CharField(max_length=1000)
    qual = models.CharField(max_length=1000)
