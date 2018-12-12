from django.db import models
from django.db.models.signals import post_save
from users.models import Registered_User, Courses, Registered_College
from django.utils import timezone
from notifications.models import Notification

class ClassPost(models.Model):
    userId = models.ForeignKey(Registered_User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    courseId = models.ForeignKey(Courses, on_delete=models.CASCADE)
    collegeId = models.ForeignKey(Registered_College, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject


class ClassImage(models.Model):
    image = models.ImageField()
    postid = models.ForeignKey(ClassPost, on_delete=models.CASCADE)

    def __str__(self):
        return self.postid.subject


class ClassComment(models.Model):
    postId = models.ForeignKey(ClassPost, on_delete=models.CASCADE)
    userId = models.ForeignKey(Registered_User, on_delete=models.DO_NOTHING)
    comment = models.TextField(default='')

    def __str__(self):
        com = self.comment[:10] + "..."
        return com


class ClassReply(models.Model):
    comId = models.ForeignKey(ClassComment, on_delete=models.CASCADE)
    userId = models.ForeignKey(Registered_User, on_delete=models.DO_NOTHING)
    reply = models.TextField(default='')

    def __str__(self):
        rep = self.reply[:10] + "..."
        return rep


class ClassLike(models.Model):
    postId = models.ForeignKey(ClassPost, on_delete=models.CASCADE)
    userId = models.ForeignKey(Registered_User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["postId", "userId"]

    def __str__(self):
        return self.userId.user.username

def Notifications_like(sender,**kwargs):
    if(kwargs['created']):
        Notification.objects.create(title='Liked',User=kwargs['instance'].postId.userId,message=kwargs['instance'].userId.First_Name+' liked your post')

def Notifications_comment(sender,**kwargs):
    if(kwargs['created']):
        Notification.objects.create(title='Commented',User=kwargs['instance'].postId.userId,message=kwargs['instance'].userId.First_Name+' Commented on your post')
    
def Notifications_reply(sender,**kwargs):
    if(kwargs['created']):
        Notification.objects.create(title='Replied',User=kwargs['instance'].postId.userId,message=kwargs['instance'].userId.First_Name+' Replied to your comment')



post_save.connect(Notifications_comment,sender=ClassComment)
post_save.connect(Notifications_like,sender=ClassLike)
post_save.connect(Notifications_reply,sender=ClassReply)

