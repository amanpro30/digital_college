from django import forms
from django.forms import ModelForm
from .models import ClassPost, ClassImage, ClassComment


class ClassPostForm(ModelForm):
    subject = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'validate text-white', }
    ))

    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder': 'Write something here...',
            'style': 'height:100px;width:100%',
        }
    ))

    class Meta:
        model = ClassPost
        fields = [
             'subject', 'content',
        ]


class ClassImageForm(ModelForm):
    image = forms.ImageField(widget=forms.FileInput(
        attrs={
            'type': 'file',
            'id': 'images'
        }
    ))

    class Meta:
        model = ClassImage
        fields = [
             'image',
        ]


class ClassCommentForm(ModelForm):
    comment = forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder': 'Post a comment..',
        }
    ))

    class Meta:
        model = ClassComment
        fields = ['comment', ]

