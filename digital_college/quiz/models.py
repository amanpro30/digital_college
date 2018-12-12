from django.db import models
from users.models import Registered_College,Registered_User,Courses
from datetime import date,time
from django.utils import timezone

# Create your models here.

class quiz(models.Model):
    college_id=models.ForeignKey(Registered_College,on_delete=models.CASCADE)
    class_id = models.ForeignKey(Courses,on_delete=models.CASCADE)
    name_of_quiz = models.CharField(max_length=50)
    instructions = models.CharField(max_length=250)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name_of_quiz
       
class multiplechoice(models.Model):
    college_id=models.ForeignKey(Registered_College,on_delete=models.CASCADE)
    class_id = models.ForeignKey(Courses,on_delete=models.CASCADE)
    quiz_id = models.ForeignKey(quiz,on_delete=models.CASCADE)
    question = models.CharField(max_length=250,)
    option1 = models.CharField(max_length=100,)
    option2 = models.CharField(max_length=100,)
    option3 = models.CharField(max_length=100,)
    option4 = models.CharField(max_length=100,)
    marks = models.IntegerField()

class answers(models.Model):
    question_id = models.ForeignKey(multiplechoice,on_delete=models.CASCADE)
    option = models.CharField(max_length=100)

class singlechoice(models.Model):
    college_id=models.ForeignKey(Registered_College,on_delete=models.CASCADE)
    class_id = models.ForeignKey(Courses,on_delete=models.CASCADE)
    quiz_id = models.ForeignKey(quiz,on_delete=models.CASCADE)
    question = models.CharField(max_length=250,)
    option1 = models.CharField(max_length=100,)
    option2 = models.CharField(max_length=100,)
    option3 = models.CharField(max_length=100,)
    option4 = models.CharField(max_length=100,)
    marks = models.IntegerField()
    answer = models.CharField(max_length=1)
    
# class matching(models.Model):
#     college_id=models.ForeignKey(Registered_College,on_delete=models.CASCADE)
#     class_id = models.ForeignKey(Courses,on_delete=models.CASCADE)
#     quiz_id = models.ForeignKey(quiz,on_delete=models.CASCADE)
#     question=models.CharField(max_length=250)
#     option1=models.CharField(max_length=100)
#     option2=models.CharField(max_length=100)
#     option3=models.CharField(max_length=100)
#     option4=models.CharField(max_length=100)
#     match1=models.CharField(max_length=100)
#     match2=models.CharField(max_length=100)
#     match3=models.CharField(max_length=100)
#     match4=models.CharField(max_length=100)
#     marks=models.IntegerField()

class truefalse(models.Model):
    college_id=models.ForeignKey(Registered_College,on_delete=models.CASCADE)
    class_id = models.ForeignKey(Courses,on_delete=models.CASCADE)
    quiz_id = models.ForeignKey(quiz,on_delete=models.CASCADE)
    question=models.CharField(max_length=250)
    option1=models.CharField(max_length=100)
    answer=models.CharField(max_length=10)
    marks=models.IntegerField()

class respo_single(models.Model):
    user_id=models.ForeignKey(Registered_User,on_delete=models.CASCADE)
    quiz_id=models.ForeignKey(quiz,on_delete=models.CASCADE)
    question_id=models.ForeignKey(singlechoice,on_delete=models.CASCADE)
    selected_option=models.CharField(max_length=20)

class respo_multiple(models.Model):
    user_id=models.ForeignKey(Registered_User,on_delete=models.CASCADE)
    quiz_id=models.ForeignKey(quiz,on_delete=models.CASCADE)
    question_id=models.ForeignKey(multiplechoice,on_delete=models.CASCADE)
    selected_option=models.CharField(max_length=20)

class respo_true(models.Model):
    user_id=models.ForeignKey(Registered_User,on_delete=models.CASCADE)
    quiz_id=models.ForeignKey(quiz,on_delete=models.CASCADE)
    question_id=models.ForeignKey(truefalse,on_delete=models.CASCADE)
    selected_option=models.CharField(max_length=20)

# class respo_match(models.Model):
#     user_id=models.ForeignKey(Registered_User,on_delete=models.CASCADE)
#     quiz_id=models.ForeignKey(quiz,on_delete=models.CASCADE)
#     question_id=models.ForeignKey(matching,on_delete=models.CASCADE)
#     selected_option=models.CharField(max_length=20)



class result(models.Model):
    quiz_id = models.ForeignKey(quiz, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Registered_User, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    total_marks = models.IntegerField()

class test_given(models.Model):
    student_id=models.ForeignKey(Registered_User,on_delete=models.CASCADE)
    quiz_id=models.ForeignKey(quiz,on_delete=models.CASCADE)