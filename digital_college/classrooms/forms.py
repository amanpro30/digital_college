from django.forms import ModelForm
from .models import quiz
from django import forms
from django.contrib.admin import widgets

class quiz_detail_form(ModelForm):
    name_of_quiz = forms.CharField( widget = forms.TextInput(attrs={'class':'validate','placeholder':'Enter the name of the quiz'}))
    instructions = forms.CharField( widget = forms.Textarea(attrs={'style':'height:100px','class':'input-fields col s7'}))
    date = forms.DateField(widget = forms.DateInput(attrs={'type':'date','class':'input-fields col s7'}))
    start_time = forms.TimeField(widget = forms.TimeInput(attrs={'type':'time','class':'input-fields col s7'}))
    end_time = forms.TimeField(widget = forms.TimeInput(attrs={'type':'time','class':'input-fields col s7'}))
    class Meta:
        model=quiz
        fields=['name_of_quiz','instructions','date','start_time','end_time']
        