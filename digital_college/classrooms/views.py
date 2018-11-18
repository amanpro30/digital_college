from django.shortcuts import render
def assignment(request):
    pass

def slides(request):
    pass


def forum(request):
    pass

def class_home(request,class_name):
    return render(request,'quiz/base_classrooms.html',{'class_name':class_name},{'class_name':class_name})
