from django.forms import ModelForm
from .models import quiz,singlechoice,multiplechoice,matching,truefalse,respo
from django import forms
from django.contrib.admin import widgets

# from .forms import 


class quiz_detail_form(ModelForm):
    name_of_quiz = forms.CharField( widget = forms.TextInput(attrs={'class':'validate','placeholder':'Enter the name of the quiz'}))
    instructions = forms.CharField( widget = forms.Textarea(attrs={'style':'height:100px','class':'input-fields col s7'}))
    class Meta:
        model=quiz
        fields=['name_of_quiz','instructions','start_time','end_time']

class single_correct_form(ModelForm):
    question = forms.CharField( widget = forms.Textarea(attrs={'class':'materialize-textarea','id':'question'}))
    option1 = forms.CharField( widget = forms.Textarea(attrs={'class':'materialize-textarea option','id':'option1'}))
    option2 = forms.CharField( widget = forms.Textarea(attrs={'class':'materialize-textarea option','id':'option2'}))
    option3 = forms.CharField( widget = forms.Textarea(attrs={'class':'materialize-textarea option','id':'option3'}))
    option4 = forms.CharField( widget = forms.Textarea(attrs={'class':'materialize-textarea option','id':'option4'}))
    # answer = forms.MultipleChoiceField(choices=ANSWER_CHOICES, widget=forms.CheckboxSelectMultiple())
    class Meta:
        model=singlechoice
        fields=['question','option1','option2','option3','option4','answer','marks']


class multi_correct_form(ModelForm):
    question = forms.CharField( widget = forms.Textarea(attrs={'class':'materialize-textarea','id':'question'}))
    option1 = forms.CharField( widget = forms.Textarea(attrs={'class':'materialize-textarea option','id':'option1'}))
    option2 = forms.CharField( widget = forms.Textarea(attrs={'class':'materialize-textarea option','id':'option2'}))
    option3 = forms.CharField( widget = forms.Textarea(attrs={'class':'materialize-textarea option','id':'option3'}))
    option4 = forms.CharField( widget = forms.Textarea(attrs={'class':'materialize-textarea option','id':'option4'}))
    class Meta:
        model=multiplechoice
        fields=['question','option1','option2','option3','option4']
    

class matching_form(ModelForm):
    question = forms.CharField( widget = forms.Textarea(attrs={'class':'materialize-textarea','id':'question'}))
    option1 = forms.CharField( widget = forms.Textarea(attrs={'class':'materialize-textarea option','id':'option1'}))
    option2 = forms.CharField( widget = forms.Textarea(attrs={'class':'materialize-textarea option','id':'option2'}))
    option3 = forms.CharField( widget = forms.Textarea(attrs={'class':'materialize-textarea option','id':'option3'}))
    option4 = forms.CharField( widget = forms.Textarea(attrs={'class':'materialize-textarea option','id':'option4'}))
    matching1 = forms.CharField( widget = forms.Textarea(attrs={'class':'materialize-textarea matching','id':'matching1'}))
    matching2 = forms.CharField( widget = forms.Textarea(attrs={'class':'materialize-textarea matching','id':'matching2'}))
    matching3 = forms.CharField( widget = forms.Textarea(attrs={'class':'materialize-textarea matching','id':'matching3'}))
    matching4 = forms.CharField( widget = forms.Textarea(attrs={'class':'materialize-textarea matching','id':'matching4'}))
    class Meta:
        model=matching
        fields=['question','option1','option2','option3','option4','match1','match2','match3','match4']

class truefalse_form(ModelForm):
    question = forms.CharField( widget = forms.Textarea(attrs={'class':'materialize-textarea','id':'question'}))
    option1 = forms.CharField( widget = forms.Textarea(attrs={'class':'materialize-textarea option','id':'option1'}))
    class Meta:
        model=truefalse
        fields=['question','option1']
    
class response_form(ModelForm):
    class Meta:
        model=respo
        fields=['selected_option']
