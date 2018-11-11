from django.db import models
from users.models import Courses,Registered_College

# Create your models here.
class quiz(models.Model):
    college_id=models.ForeignKey(Registered_College,on_delete=models.CASCADE)
    class_id = models.ForeignKey(Courses,on_delete=models.CASCADE)
    name_of_quiz = models.CharField(max_length=50)
    instructions = models.CharField(max_length=250)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    total_marks = models.IntegerField()
    
    def __str__(self):
        return self.name

class multiplechoice(models.Model):
    college_id=models.ForeignKey(Registered_College,on_delete=models.CASCADE)
    class_id = models.ForeignKey(Courses,on_delete=models.CASCADE)
    quiz_id = models.ForeignKey(quiz,on_delete=models.CASCADE)
    question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)

class answers(models.Model):
    college_id=models.ForeignKey(Registered_College,on_delete=models.CASCADE)
    question_id = models.ForeignKey(multiplechoice,on_delete=models.CASCADE)
    option = models.IntegerField()

class singlechoice(models.Model):
    college_id=models.ForeignKey(Registered_College,on_delete=models.CASCADE)
    class_id = models.ForeignKey(Courses,on_delete=models.CASCADE)
    quiz_id = models.ForeignKey(quiz,on_delete=models.CASCADE)
    question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.IntegerField()

class matching(models.Model):
    college_id=models.ForeignKey(Registered_College,on_delete=models.CASCADE)
    class_id = models.ForeignKey(Courses,on_delete=models.CASCADE)
    quiz_id = models.ForeignKey(quiz,on_delete=models.CASCADE)
    question=models.CharField(max_length=250)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    match1=models.CharField(max_length=100)
    match2=models.CharField(max_length=100)
    match3=models.CharField(max_length=100)
    match4=models.CharField(max_length=100)

class truefalse(models.Model):
    college_id=models.ForeignKey(Registered_College,on_delete=models.CASCADE)
    class_id = models.ForeignKey(Courses,on_delete=models.CASCADE)
    quiz_id = models.ForeignKey(quiz,on_delete=models.CASCADE)
    question=models.CharField(max_length=250)
    option1=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)