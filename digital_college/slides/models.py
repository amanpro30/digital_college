from django.db import models
from users.models import Registered_College,Courses
# Create your models here.

from django.db import models
from django.urls import reverse
# Create your models here.
class assign(models.Model):
    file = models.FileField(upload_to='media/faculty')
    title = models.CharField(max_length=100)
    college_id = models.ForeignKey(Registered_College,on_delete=models.CASCADE)
    course_id = models.ForeignKey(Courses,on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse("assign",kwargs={"file":self.file})
