from django import forms

from .models import assign, assign_solution


class add_assign(forms.ModelForm):
    file = forms.FileField(widget=forms.FileInput())
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'blue-text text-darken-4',
        'style': 'width:60%;',
        'placeholder': 'Add Title'}
    ))

    class Meta:
        model = assign
        fields = [
            'title', 'file', 'deadline',
        ]


class add_assign_solution(forms.ModelForm):
    class Meta:
        model = assign_solution
        fields = [
            'file'
        ]
