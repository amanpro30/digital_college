from django.db import models
from users.models import Registered_User, Courses, Exam
# Create your models here.


class ExamResult(models.Model):
    userId = models.ForeignKey(Registered_User, on_delete=models.CASCADE)
    courseId = models.ForeignKey(Courses, on_delete=models.CASCADE)
    examId = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()


