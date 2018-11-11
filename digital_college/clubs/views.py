from django.shortcuts import render
from clubs.models import Post, Images
from .form import PostForm, ImageForm
from users.models import Registered_User


def home(request):
    posts = Post.objects.all()
    imageform = ImageForm()
    postform = PostForm()
    context = {
        'imageform': imageform,
        'postform': postform,
        'posts': posts,
    }
    return render(request, 'clubs/club_forum.html', context)


def contacts(request):
    pass


def gallery(request):
    pass


def post(request):
    if request.method == 'POST':
        postform = PostForm(request.POST)
        imageform = ImageForm(request.POST, request.FILES)
        if postform.is_valid() and imageform.is_valid():
            subject = postform.cleaned_data['subject']
            content = postform.cleaned_data['content']
            date = postform.cleaned_data['date']
            user = Registered_User.objects.get(user=request.user)
            a = Post(userId=user, subject=subject, content=content, date=date)
            a.save()
            b = Images(image=request.FILES['image'], postId=a)
            b.save()
    else:
        imageform = ImageForm()
        postform = PostForm()
    posts = Post.objects.all()
    context = {
        'user': request.user,
        'imageform': imageform,
        'postform': postform,
        'posts': posts,
    }
    return render(request, 'clubs/club_forum.html', context)


def progress_report(request):
    return None


def delete(request, post_id):
    Post.objects.get(id=post_id).delete()
    posts = Post.objects.all()
    return render(request, 'clubs/club_forum.html', {'posts': posts})


def update(request):
    return None


def after_login(request):
    return None
