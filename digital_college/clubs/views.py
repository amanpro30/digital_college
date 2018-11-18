from django.shortcuts import render
from clubs.models import Post, Images, Like
from .form import PostForm, ImageForm
from users.models import Registered_User


def home(request):
    posts = Post.objects.all().order_by('-date')
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
            user = Registered_User.objects.get(user=request.user)
            a = Post(userId=user, subject=subject, content=content,)
            a.save()
            b = Images(image=request.FILES['image'], postId=a)
            b.save()
    else:
        imageform = ImageForm()
        postform = PostForm()
    posts = Post.objects.all().order_by('-date')
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
    posts = Post.objects.all().order_by('-date')
    imageform = ImageForm()
    postform = PostForm()
    context = {
        'imageform': imageform,
        'postform': postform,
        'posts': posts,
    }
    return render(request, 'clubs/club_forum.html', context)


def like_post(request, post_id):
    posts = Post.objects.all().order_by('-date')
    imageform = ImageForm()
    postform = PostForm()
    context = {
        'imageform': imageform,
        'postform': postform,
        'posts': posts,
    }
    a = Like(postId=post_id, userId=request.user)
    a.save()
    return render(request, 'clubs/club_forum.html', context)


def update(request):
    return None


def after_login(request):
    return None
