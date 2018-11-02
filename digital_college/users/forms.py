from django.forms import ModelForm
from .models import Registered_User,Registered_College
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import HttpResponseRedirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm




class User_Registration_Form(ModelForm):
    ROLE_CHOICES=(
        ('F','Faculty'),
        ('S','Student')
    )
    role=forms.ChoiceField(choices=ROLE_CHOICES)
    college_id=forms.ModelChoiceField(queryset=Registered_College.objects.all())
    class Meta:
        model=Registered_User
        fields=['email','role','college_id','activation_key',]

class College_Registration_Form(ModelForm):
    STATE_CHOICES=(
        ('AP','Andhra Pradesh'),
        ('AC','Arunchal Pradesh'),
        ('AS','Assam'),
        ('BR','Bihar'),
        ('CH','Chattisgarh'),
        ('GO','Goa'),
        ('GJ','Gujarat'),
        ('HR','Haryana'),
        ('HP','Himachal Pradesh'),
        ('JK','Jammu and Kashmir'),
        ('JH','Jharkhand'),
        ('KN','Karnataka'),
        ('KL','Kerala'),
        ('MP','Madhya Pradesh'),
        ('MH','Maharastra'),
        ('MN','Manipur'),
        ('MZ','Mizoram'),
        ('MG','Meghalaya'),
        ('NG','Nagaland'),
        ('OR','Orissa'),
        ('PB','Punjab'),
        ('RJ','Rajasthan'),
        ('SK','Sikkim'),
        ('TN','Tamil Nadu'),
        ('TG','Telangana'),
        ('TP','Tripura'),
        ('UL','Uttaranchal'),
        ('UP','Uttar Pradesh'),
        ('WB','West Bengal')
    )
    email=forms.CharField(widget=forms.EmailInput)
    State=forms.ChoiceField(choices=STATE_CHOICES)
    class Meta:
        model = Registered_College
        fields = ['Name_Of_College', 'email', 'College_Registration_Number', 'City', 'State']

def Sign_Up_Form(UserCreationForm):
    email=forms.CharField(widget=forms.EmailInput)
    class Meta:
        model=UserCreationForm
        fields=['username','first_name','last_name','email','password1','password2']

