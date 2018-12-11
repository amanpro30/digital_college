from django import forms
from django.forms import ModelForm
from .models import ClassPost, ClassImage, ClassComment, ClassReply


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
            'id': 'images',
            'accept': '.jpg',
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


class ClassReplyForm(ModelForm):
    reply = forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder': 'Reply..',
        }
    ))

    class Meta:
        model = ClassReply
        fields = ['reply', ]


class ClassPostUpdateForm(ModelForm):
    class Meta:
        model = ClassPost
        fields = ['subject', 'content', ]
