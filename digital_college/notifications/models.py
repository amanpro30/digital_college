from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Notification(models.Model):
    title=models.CharField(max_length=250)
    message=models.CharField(max_length=256)
    viewed=models.BooleanField(default=False)
    User=models.ForeignKey(User,on_delete=models.CASCADE)


# @receiver (post_save,sender=User)
# def create welcome_message(sender,**kwargs):
#     if kwargs.get('created',False):
#         Notification.objects.create(user=kwargs.get('instance'),title='Welcome',message='Thanks')
#         pass
