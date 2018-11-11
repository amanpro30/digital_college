from django.shortcuts import render
from .forms import quiz_detail_form
from .models import quiz as qz,singlechoice,multiplechoice,matching,truefalse,answers
from datetime import datetime
from django.contrib.auth.models import User
import pytz

# Create your views here.



def quiz(request):
    print(request.user.registered_user.college_id)
    # print((request.user.registered_college))
    if request.method=='POST':
        form = quiz_detail_form(request.POST)
        if form.is_valid():
            form.save()
        
    else:
        form=quiz_detail_form()
    Quiz= qz.objects.all().first()
    def is_started(quiz):
        present=datetime.utcnow()
        present = pytz.utc.localize(present)
        return quiz.start_time < present
    def is_finished(quiz):
        present=datetime.utcnow()
        present = pytz.utc.localize(present)
        return quiz.end_time < present
    single = singlechoice.objects.filter(college_id=request.user.registered_user.college_id,class_id=request.user.registered_college.)
    multiple = multiplechoice.objects.filter(college_id=request.user.registered_user.college_id,class_id=)
    tf = truefalse.objects.filter(college_id=request.user.registered_user.college_id,class_id=)
    match = matching.objects.filter(college_id=request.user.registered_user.college_id,class_id=)
    ans = answers.objects.filter(college_id=request.user.registered_user.college_id,class_id=)
    return render(request,'classrooms/quiz.html',{'quiz_detail_form':form,'is_started':is_started(Quiz),'is_finished':is_finished(Quiz),'qz':Quiz})

def assignment(request):
    pass

def slides(request):
    pass


def forum(request):
    pass