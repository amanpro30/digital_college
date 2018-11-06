from django.shortcuts import render
from clubs.models import Post, Images
from .form import PostForm, ImageForm


def home(request):
    posts = Post.objects.all()
    images = Images.objects.all()
    return render(request, 'clubs/club_forum.html', {'posts': posts, 'images': images})


def contacts(request):
    pass


def gallery(request):
    pass


# def post(request):
#     # user = request.user
#     if request.method == 'POST':
#         subject = request.POST.get('subject1')
#         content = request.POST.get('content')
#         images = request.POST.get('images')
#         a = Post(subject=subject, content=content)
#         a.save()
#         for img in images:
#             b = Images(postId=a.pk, image=img)
#             b.save()
#         print("in Post")
#     data = Post.objects.all()
#     return render(request, 'clubs/club_forum.html', {'data': data})

def post(request):
    pass


'''
def post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        image_form = ImageForm(request.POST)
        if post_form.is_valid() and image_form.is_valid():
            post_form.save()
            image_form.save()
    else:
        post_form = PostForm()
        image_form = ImageForm()
    return render (request,'clubs/club_basic.html',{'post_form':post_form, 'image_form':image_form})

'''