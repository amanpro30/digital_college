from django.shortcuts import render

from forum.form import ClassPostForm, ClassImageForm, ClassCommentForm
from forum.models import ClassPost
from users.models import Courses


def forum(request, class_name):
    user = request.user
    if request.method == 'POST':
        postform = ClassPostForm(request.POST)
        if postform.is_valid():
            a = ClassPost(userId=user.registered_user, collegeId=user.registered_user.college_id,
                          courseId=Courses.objects.get(course_name=class_name),
                          subject=postform.cleaned_data['subject'], content=postform.cleaned_data['content'])
            a.save()
    else:
        postform = ClassPostForm()
    classId = Courses.objects.get(course_name=class_name)
    posts = ClassPost.objects.filter(courseId=classId)
    context = {
        'posts': posts,
        'class_name': class_name,
        'postform': postform,
        'imageform': ClassImageForm(),
        'commentform': ClassCommentForm(),
    }
    return render(request, 'forum/classpost.html', context)
