from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Entry(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.date}'
