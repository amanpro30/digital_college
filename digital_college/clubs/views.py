from django.shortcuts import render, redirect
from clubs.models import Post, Images, Like, Comment
from .form import PostForm, ImageForm, CommentForm, PostUpdateForm, ImageUpdateForm, CommentUpdateForm
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
            return redirect(request.META.get('HTTP_REFERER'), club_name)
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


def delete(request, club_name, post_id):
    Post.objects.get(id=post_id).delete()
    return redirect(request.META.get('HTTP_REFERER'), club_name)


def like_post(request, club_name, post_id):
    a = Like.objects.create(postId=Post.objects.get(pk=post_id), userId=Registered_User.objects.get(user=request.user))
    a.save()
    return redirect(request.META.get('HTTP_REFERER'), club_name)


def dislike_post(request, club_name, post_id):
    Like.objects.filter(postId=Post.objects.get(pk=post_id),
                        userId=Registered_User.objects.get(user=request.user)).delete()
    return redirect(request.META.get('HTTP_REFERER'), club_name)


def comment(request, club_name, post_id):
    if request.method == 'POST':
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            comment = commentform.cleaned_data['comment']
            user = Registered_User.objects.get(user=request.user)
            b = Comment(postId=Post.objects.get(pk=post_id), comment=comment, userId=user)
            b.save()
            return redirect(request.META.get('HTTP_REFERER'), club_name)
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


def postdetail(request, club_name, post_id):
    context = {
        'club_name': club_name,
        'post': Post.objects.get(id=post_id),
        'commentform': CommentForm(),
        'p_up_form': PostUpdateForm(instance=Post.objects.get(id=post_id))
    }
    return render(request, 'after_login/seepost.html', context)


def update(request, club_name, post_id):
    if request.method == 'POST':
        post_update_form = PostUpdateForm(request.POST, instance=Post.objects.get(id=post_id))
        # image_update_form = ImageUpdateForm(request.POST, request.FILES, instance=Images.objects.filter)
        if post_update_form.is_valid():
            post_update_form.save()
    return redirect(request.META.get('HTTP_REFERER'), club_name)


def delcom(request, club_name, com_id):
    Comment.objects.get(id=com_id).delete()
    return redirect(request.META.get('HTTP_REFERER'), club_name)
