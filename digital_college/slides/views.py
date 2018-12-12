from django.shortcuts import render, get_object_or_404, redirect
from .models import assign,assign_solution
from django.http import HttpResponse
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from .forms import add_assign,add_assign_solution
from users.models import Courses
from django.contrib.auth.models import User
from django.contrib import messages

from django.core.files.storage import FileSystemStorage


def download(request, class_name, id=None):
    instance = assign.objects.get(id=id)
    file_path = instance.file.url
    file_path = file_path[1:]
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf , application/")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def addSlides(request, class_name):
    course_instance = Courses.objects.get(course_name=class_name)
    slides_files = assign.objects.filter(ass_type='slides')
    form = add_assign(request.POST or None, request.FILES or None)
    if form.is_valid():
        newAssign = form.save(commit=False)
        newAssign.course_id=course_instance
        newAssign.ass_type='slides'
        newAssign.save()
    context = {
        "form": form,
        "slides_files":slides_files,
        "class_name": class_name,
    }
    return render(request, 'slides/slides.html', context)

def addAssign(request,class_name):
    if request.method=='POST':
        form = add_assign(request.POST or None, request.FILES or None)
        assign_solution_form=assign_solution_form(request.POST)
        if form.is_valid():
            newAssign = form.save(commit=False)
            newAssign.course_id = course_instance
            newAssign.ass_type = 'slides'
            newAssign.save()
        if assign_solution_form.is_valid():
            newAssign = form.save(commit=False)
            newAssign.assignment_id = last_assign_file
            newAssign.student_id=user_instance
            newAssign.save()
    else:
        username=request.user
        user_instance=User.objects.get(username=username)
        form = add_assign()
        course_instance = Courses.objects.get(course_name=class_name)
        last_assign_file= assign.objects.filter(ass_type='assign').last()
        assign_solution_files=assign_solution.objects.filter(assignment_id=last_assign_file)
        assign_solution_form=add_assign_solution()
        assign_solution_form = assign_solution_form()
        context={
            'form':form,
            "last_assign_file": last_assign_file,
            'assign_solution_files': assign_solution_files,
            'class_name':class_name,
            'assign_solution_form':assign_solution_form,
        }
    return render(request,'slides/assignment.html',context)

def delSlides(request, class_name, file_id):
    assign.objects.get(pk=file_id).delete()
    # return redirect ('/classrooms/{k}/slides/addSlides/'.format(k=class_name))
    return redirect('users:after:classroom:slides:addSlides', class_name=class_name)
