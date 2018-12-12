from django import forms
from django.forms import ModelForm

from calendarapp.models import Entry


class Entryform(forms.Form):
    name = forms.CharField(max_length=100)
    date = forms.DateTimeField()
    description = forms.CharField(widget=forms.Textarea)

class EntryUpdateForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['name', 'date', 'description']

