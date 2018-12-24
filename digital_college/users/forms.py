from django.forms import ModelForm
from .models import Registered_User, Registered_College, Courses
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import Registered_User, Registered_College,Announcement


class User_Registration_Form(ModelForm):
    ROLE_CHOICES = (
        ('F', 'Faculty'),
        ('S', 'Student')
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect())
    college_id = forms.ModelChoiceField(queryset=Registered_College.objects.all())
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Registered_User
        fields = ['role', 'email', 'First_Name', 'Last_Name', 'college_id', 'image', ]



class College_Registration_Form(ModelForm):
    STATE_CHOICES = (
        ('AP', 'Andhra Pradesh'),
        ('AC', 'Arunchal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CH', 'Chattisgarh'),
        ('GO', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JK', 'Jammu and Kashmir'),
        ('JH', 'Jharkhand'),
        ('KN', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharastra'),
        ('MN', 'Manipur'),
        ('MZ', 'Mizoram'),
        ('MG', 'Meghalaya'),
        ('NG', 'Nagaland'),
        ('OR', 'Orissa'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TG', 'Telangana'),
        ('TP', 'Tripura'),
        ('UL', 'Uttaranchal'),
        ('UP', 'Uttar Pradesh'),
        ('WB', 'West Bengal')
    )
    State = forms.ChoiceField(choices=STATE_CHOICES)

    class Meta:
        model = Registered_College
        fields = ['Name_Of_College', 'email', 'College_Registration_Number', 'City', 'State', 'image', ]


def Sign_Up_Form(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput)

    class Meta:
        model = UserCreationForm
        fields = ['username', 'email', 'password1', 'password2']


class User_reset_form(ModelForm):
    username = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = User
        fields = ['username', 'password', ]


class Course_Forms(forms.ModelForm):
    faculty_id = forms.ModelChoiceField(queryset=Registered_User.objects.all())
    college_id = forms.ModelChoiceField(queryset=Registered_College.objects.all())

    class Meta:
        model = Courses
        fields = ['course_name', 'college_id', 'faculty_id']


class Edit_Registered_User_Form(forms.ModelForm):
    class Meta:
        model = Registered_User
        fields = ['First_Name', 'Last_Name', 'college_id', 'image', ]


class Edit_Registered_College_Form(forms.ModelForm):
    class Meta:
        model = Registered_College
        fields = ['Name_Of_College', 'City', 'State', 'image', ]


class ResetForm(forms.Form):
    enter_email = forms.EmailField()


class ResetDoneForm(forms.Form):
    Password = forms.CharField(widget=forms.PasswordInput())
    Confirm_Password = forms.CharField(widget=forms.PasswordInput())


class Announcement_Form(ModelForm):
    class Meta:
        model = Announcement
        fields = ['Title', 'Description', 'Date',]

class Choice_Form(forms.Form):
    ROLE_CHOICES = (
        ('A', 'ADMIN'),
        ('U', 'USER')
    )
    Please_Select_Your_Role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect())