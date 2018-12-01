from django.forms import ModelForm
from django import forms
from users.models import Registered_User, Clubs


class ClubForm(ModelForm):
    club_name = forms.CharField(widget=forms.TextInput(attrs={
        'style': 'width:70%;',
        'class': 'teal-text',
    }))
    club_head = forms.ModelChoiceField(queryset=Registered_User.objects.filter(role='S'))

    caption1 = forms.CharField(widget=forms.TextInput(attrs={
        'style': 'width:70%;',
        'class': 'teal-text',
    }))
    caption2 = forms.CharField(widget=forms.TextInput(attrs={
        'style': 'width:70%;',
        'class': 'teal-text',
    }))
    caption3 = forms.CharField(widget=forms.TextInput(attrs={
        'style': 'width:70%;',
        'class': 'teal-text',
    }))

    class Meta:
        model = Clubs
        fields = ['club_name', 'club_head', 'image1', 'image2', 'image3', 'caption1', 'caption2', 'caption3']





