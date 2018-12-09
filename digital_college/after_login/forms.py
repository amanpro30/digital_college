from django.forms import ModelForm
from django import forms

from clubs.models import ClubSlideShowInfo
from users.models import Registered_User, Clubs, Courses


class ClubForm(ModelForm):
    club_name = forms.CharField(widget=forms.TextInput(attrs={
        'style': 'width:70%;',
        'class': 'teal-text',
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

