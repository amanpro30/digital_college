from django import forms

from .models import assign

class add_assign(forms.ModelForm):
    file = forms.FileField(widget=forms.FileInput())
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'col s2','placeholder':'Add Title'}))
    class Meta:
        model = assign
        fields=[
            'title','file'
        ]