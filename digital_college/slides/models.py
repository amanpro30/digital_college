from django.db import models
from django.urls import reverse
from users.models import Courses, Registered_User
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class assign(models.Model):
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    CHOICES = (
        ('assign', 'assign'),
        ('slides', 'slides'),
    )
    file = models.FileField(upload_to='media/faculty')
    title = models.CharField(max_length=100)
    ass_type = models.CharField(max_length=15, choices=CHOICES, default='answer')
    deadline = models.DateTimeField(default=timezone.now, blank=True)

    def get_absolute_url(self):
        return reverse("assign", kwargs={"file": self.file})


class assign_solution(models.Model):
    student_id = models.ForeignKey(Registered_User, on_delete=models.CASCADE)
    assignment_id = models.ForeignKey(assign, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/faculty')
