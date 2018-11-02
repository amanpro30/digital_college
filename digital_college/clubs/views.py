from django.shortcuts import render
from .models import Post


def home(request):
    data = Post.objects.all()
    return render(request, 'clubs/club_basic.html', {'data': data})


def forum(request):
    return render(request, 'clubs/club_forum.html')


def contacts(request):
    pass


def post(request):
    return render(request, 'clubs/club_post.html')


def gallery(request):
    pass
