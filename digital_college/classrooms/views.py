from django.shortcuts import render
from .forms import quiz_detail_form


# Create your views here.
def quiz(request):
    if request.method=='POST':
        form = quiz_detail_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=quiz_detail_form()
    return render(request,'classrooms/quiz.html',{'quiz_detail_form':form})

def assignment(request):
    pass

def slides(request):
    pass


def forum(request):
    pass