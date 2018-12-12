from django.forms import ModelForm
from django import forms

from clubs.models import ClubSlideShowInfo
from users.models import Registered_User, Clubs, Courses, Email, UploadedFiles, Registered_College


class ClubForm(ModelForm):
    club_name = forms.CharField(widget=forms.TextInput(attrs={
        'style': 'width:70%;',
        'class': 'blue-text text-darken-4',
    }))
    club_head = forms.ModelChoiceField(queryset=Registered_User.objects.filter(role='S'))

    class Meta:
        model = Clubs
        fields = ['club_name', 'club_head']


class SlideShowDetails:
    class Meta:
        model = ClubSlideShowInfo
        fields = ['image', 'heading', 'caption']


class CourseForm(ModelForm):
    course_name = forms.CharField(widget=forms.TextInput(attrs={
        'style': 'width:70%;',
        'class': 'teal-text',
    }))
    faculty_id = forms.ModelChoiceField(queryset=Registered_User.objects.filter(role='F'))

    class Meta:
        model = Courses
        fields = ['course_name', 'faculty_id']


class EmailForm(ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'id': 'email',
    }))

    class Meta:
        model = Email
        fields = ['email']


class UploadFileForm(ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'file-path validate',
    }))
    file = forms.FileField(widget=forms.FileInput(attrs={
        'accept': '.csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel',
    }))

    class Meta:
        model = UploadedFiles
        fields = ['file']
