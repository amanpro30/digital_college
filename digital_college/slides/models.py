from django.db import models
from django.urls import reverse
# Create your models here.
class assign(models.Model):
    file = models.FileField(upload_to='media/faculty')
    title = models.CharField(max_length=100)
    def get_absolute_url(self):
        return reverse("assign",kwargs={"file":self.file})
