from django.db import models
from users.models import Registered_College
from django.utils import timezone
# Create your models here.

class announcements(models.Model):
    college_id=models.ForeignKey(Registered_College,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)
    message=models.CharField(max_length=250)