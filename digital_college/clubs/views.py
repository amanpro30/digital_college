from django.shortcuts import render
from clubs.models import Post, Images, Like, Comment
from .form import PostForm, ImageForm, CommentForm
from users.models import Registered_User, Clubs


def contacts(request, club_name):
    pass


def gallery(request, club_name):
    imageform = ImageForm()
    postform = PostForm()
    images = Images.objects.all()
    context = {
        'club_name': club_name,
        'user': request.user,
        'imageform': imageform,
        'postform': postform,
        'images': images,
    }

    return render(request, 'clubs/club_gallery.html', context)


def post(request, club_name):
    if request.method == 'POST':
        postform = PostForm(request.POST)
        imageform = ImageForm(request.POST, request.FILES)
        if postform.is_valid() and imageform.is_valid():
            subject = postform.cleaned_data['subject']
            content = postform.cleaned_data['content']
            user = Registered_User.objects.get(user=request.user)
            club_id = Clubs.objects.get(club_name=club_name)
            a = Post(userId=user, subject=subject, content=content, collegeId=user.college_id, clubId=club_id)
            a.save()
            b = Images(image=request.FILES['image'], postId=a)
            b.save()
    else:
        imageform = ImageForm()
        postform = PostForm()
    commentform = CommentForm()
    club_id = Clubs.objects.get(club_name=club_name)
    posts = Post.objects.filter(clubId=club_id).order_by('-date')
    context = {
        'club_name': club_name,
        'user': request.user,
        'imageform': imageform,
        'postform': postform,
        'posts': posts,
        'commentform': commentform,
    }
    return render(request, 'clubs/club_forum.html', context)


def post_mob(request, club_name):
    imageform = ImageForm()
    postform = PostForm()
    context = {
        'club_name': club_name,
        'user': request.user,
        'imageform': imageform,
        'postform': postform,
    }
    return render(request, 'clubs/club_post_mob.html', context)


def progress_report(request, club_name):
    return None


def delete(request, club_name, post_id):
    Post.objects.get(id=post_id).delete()
    club_id = Clubs.objects.get(club_name=club_name)
    posts = Post.objects.filter(clubId=club_id).order_by('-date')
    imageform = ImageForm()
    postform = PostForm()
    commentform = CommentForm()
    context = {
        'club_name': club_name,
        'imageform': imageform,
        'postform': postform,
        'posts': posts,
        'commentform': commentform,
    }
    return render(request, 'clubs/club_forum.html', context)


def like_post(request, club_name, post_id):
    club_id = Clubs.objects.get(club_name=club_name)
    posts = Post.objects.filter(clubId=club_id).order_by('-date')
    imageform = ImageForm()
    postform = PostForm()
    commentform = CommentForm()
    context = {
        'club_name': club_name,
        'imageform': imageform,
        'postform': postform,
        'posts': posts,
        'commentform': commentform,
    }
    a = Like.objects.create(postId=Post.objects.get(pk=post_id), userId=Registered_User.objects.get(user=request.user))
    a.save()
    return render(request, 'clubs/club_forum.html', context)


def update(request, club_name):
    return None


def after_login(request, club_name):
    return None


def dislike_post(request, club_name, post_id):
    Like.objects.filter(postId=Post.objects.get(pk=post_id),
                        userId=Registered_User.objects.get(user=request.user)).delete()
    club_id = Clubs.objects.get(club_name=club_name)
    posts = Post.objects.filter(clubId=club_id).order_by('-date')
    imageform = ImageForm()
    postform = PostForm()
    commentform = CommentForm()
    context = {
        'club_name': club_name,
        'imageform': imageform,
        'postform': postform,
        'posts': posts,
        'commentform': commentform,
    }
    return render(request, 'clubs/club_forum.html', context)


def comment(request, club_name, post_id):
    if request.method == 'POST':
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            comment = commentform.cleaned_data['comment']
            print(comment)
            user = Registered_User.objects.get(user=request.user)
            b = Comment(postId=Post.objects.get(pk=post_id), comment=comment, userId=user)
            b.save()
    else:
        commentform = CommentForm()
    imageform = ImageForm()
    postform = PostForm()
    club_id = Clubs.objects.get(club_name=club_name)
    posts = Post.objects.filter(clubId=club_id).order_by('-date')
    context = {
        'club_name': club_name,
        'user': request.user,
        'imageform': imageform,
        'postform': postform,
        'posts': posts,
        'commentform': commentform,
    }
    return render(request, 'clubs/club_forum.html', context)
