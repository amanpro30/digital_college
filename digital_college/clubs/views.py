from django.shortcuts import render
from .models import Post


def clubs(request):
    data = Post.objects.all()
    return render(request, 'clubs/clubs_page.html', {'data': data})
