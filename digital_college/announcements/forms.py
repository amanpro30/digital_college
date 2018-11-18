from django.forms import ModelForm
from .models import announcements
from django import forms

class announcement_form(ModelForm):
    message=forms.CharField(widget=forms.Textarea())
    class Meta:
        model=announcements
        fields=['message']