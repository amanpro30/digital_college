from django import forms
from django.forms import ModelForm
from .models import Post, Images


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'userId', 'date', 'subject', 'content',
        ]


class ImageForm(ModelForm):
    image = forms.ImageField(widget=forms.FileInput(
        attrs={
            'type': 'file',
            'id': 'images'
        }
    ))

    class Meta:
        model = Images
        fields = [
            'postId', 'image',
        ]
