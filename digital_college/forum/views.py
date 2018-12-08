from django.shortcuts import render, redirect

from forum.form import ClassPostForm, ClassImageForm, ClassCommentForm
from forum.models import ClassPost, ClassImage, ClassComment, ClassLike
from users.models import Courses


def forum(request, class_name):
    user = request.user
    if request.method == 'POST':
        postform = ClassPostForm(request.POST)
        imageform = ClassImageForm(request.POST, request.FILES)
        print(postform.is_valid(), imageform.is_valid())
        print(postform.errors, imageform.errors)
        if postform.is_valid() and imageform.is_valid():
            a = ClassPost(userId=user.registered_user, collegeId=user.registered_user.college_id,
                          courseId=Courses.objects.get(course_name=class_name),
                          subject=postform.cleaned_data['subject'], content=postform.cleaned_data['content'])
            a.save()
            b = ClassImage(image=request.FILES['image'], postid=a)
            b.save()
            return redirect(request.META.get('HTTP_REFERER'), class_name)
    else:
        postform = ClassPostForm()
        imageform = ClassImageForm()
    classId = Courses.objects.get(course_name=class_name, college_id=user.registered_user.college_id)
    posts = ClassPost.objects.filter(courseId=classId)
    context = {
        'posts': posts,
        'class_name': class_name,
        'postform': postform,
        'imageform': imageform,
        'commentform': ClassCommentForm(),
    }
    return render(request, 'forum/classpost.html', context)


def comment(request, class_name, post_id):
    user = request.user
    if request.method == 'POST':
        commentform = ClassCommentForm(request.POST)
        if commentform.is_valid():
            a = ClassComment(postId=ClassPost.objects.get(id=post_id), userId=user.registered_user,
                             comment=commentform.cleaned_data['comment'])
            a.save()
            return redirect(request.META.get('HTTP_REFERER'), class_name)

    else:
        commentform = ClassCommentForm()
    postform = ClassPostForm()
    imageform = ClassImageForm()
    classId = Courses.objects.get(course_name=class_name, college_id=user.registered_user.college_id)
    posts = ClassPost.objects.filter(courseId=classId)
    context = {
        'posts': posts,
        'class_name': class_name,
        'postform': postform,
        'imageform': imageform,
        'commentform': commentform,
    }
    return render(request, 'forum/classpost.html', context)


def delete(request, class_name, post_id):
    ClassPost.objects.get(id=post_id).delete()
    return redirect(request.META.get('HTTP_REFERER'), class_name)


def postdetails(request, class_name, post_id):
    context = {
        'class_name': class_name,
        'post': ClassPost.objects.get(id=post_id),
        'commentform': ClassCommentForm(),
        # 'p_up_form': PostUpdateForm(instance=Post.objects.get(id=post_id))
    }
    return render(request, 'forum/post_details.html', context)


def delcom(request, class_name, com_id):
    ClassComment.objects.get(id=com_id).delete()
    return redirect(request.META.get('HTTP_REFERER'), class_name)


def like_post(request, class_name, post_id):
    user = request.user
    a = ClassLike.objects.create(postId=ClassPost.objects.get(pk=post_id), userId=user.registered_user)
    a.save()
    return redirect(request.META.get('HTTP_REFERER'), class_name)


def dislike_post(request, class_name, post_id):
    user = request.user
    ClassLike.objects.filter(postId=ClassPost.objects.get(pk=post_id),
                             userId=user.registered_user).delete()
    return redirect(request.META.get('HTTP_REFERER'), class_name)
