from django.db import models
from django.contrib.auth.models import User
from django import forms

class Registered_College(models.Model):
    Name_Of_College=models.CharField(max_length=100)
    Password=models.CharField(max_length=50)
    Email_Id=models.EmailField()
    College_Registration_Number=models.IntegerField()
    City=models.CharField(max_length=25)
    State=models.CharField(max_length=25)
    def __str__(self):
        return self.Name_Of_College

class Registered_User(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    activation_key=models.CharField(max_length=255)
    email_validated=models.BooleanField(default=False)
    email=models.EmailField(max_length=50)
    ROLE_CHOICES=[
        ('F','faculty'),
        ('S','student'),
    ]
    role=models.CharField(max_length=1,choices=ROLE_CHOICES)
    college_id=models.ForeignKey(Registered_College,on_delete=models.CASCADE,default=0)
    def __str__(self):
        return self.user.username

class Clubs(models.Model):
    club_name=models.CharField(max_length=100)
    club_head=models.ForeignKey(Registered_User,on_delete=models.CASCADE)
    def __str__(self):
        return self.club_name

class Courses(models.Model):
    course_name=models.CharField(max_length=100)
    faculty_id=models.ForeignKey(Registered_User,on_delete=models.CASCADE)
    def __str__(self):
        return self.course_name

class Registered_Emails(models.Model):
    mails=models.EmailField(null=False)
    def __str__(self):
        return self.mails

class ClubEnrollment(models.Model):
    club_id=models.ForeignKey(Clubs,on_delete=models.CASCADE)
    student_id=models.ForeignKey(Registered_User,on_delete=models.CASCADE)

class CourseEnrollment(models.Model):
    course_id=models.ForeignKey(Courses,on_delete=models.CASCADE)
    student_id=models.ForeignKey(Registered_User,on_delete=models.CASCADE)
