from django import forms
from django.forms import ModelForm
from .models import Post, Images, Comment


class PostForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder': 'Write something here...',
            'style': 'height:100px;width:100%',
        }
    ))

    class Meta:
        model = Post
        fields = [
            'subject', 'content',
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
            'image',
        ]


class CommentForm(ModelForm):
    comment = forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder': 'Post a comment..',
        }
    ))

    class Meta:
        model = Comment
        fields = ['comment', ]


class PostUpdateForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'style': 'height:100px;width:100%',
        }
    ))

    class Meta:
        model = Post
        fields = [
            'subject', 'content',
        ]


class ImageUpdateForm(ModelForm):

    class Meta:
        model = Images
        fields = [
            'image',
        ]


class CommentUpdateForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['comment', ]






