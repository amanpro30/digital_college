from django.shortcuts import render

from datetime import datetime
from django.contrib.auth.models import User
import pytz

# Create your views here.




def assignment(request):
    pass

def slides(request):
    pass


def forum(request):
    pass

def class_home(request,class_name):
    return render(request,'quiz/base_classrooms.html',{'class_name':class_name},{'class_name':class_name})

