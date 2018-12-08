from django.db import models
from users.models import Registered_User, Courses, Exam
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Create your models here.


class ExamResult(models.Model):
    userId = models.ForeignKey(Registered_User, on_delete=models.CASCADE)
    examId = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()


def populateExamResult(sender,**kwargs):
    if(kwargs['created']):
        F = open(kwargs['instance'].result_file.url[1:], mode='r')
        try:
            line = F.readlines()
            data = []
            for i in line:
                buffer1 = i.split("\n")
                buffer1 = buffer1[0].split('\t')
                buffer1 = buffer1[0].split(',')
                data.append(buffer1)
        finally:
            F.close()
        for d in data:
            user_instance=Registered_User.objects.get(pk=int(d[0]))
            ExamResult.objects.create(userId=user_instance, examId=kwargs['instance'], marks_obtained=d[1])


post_save.connect(populateExamResult,sender=Exam)
