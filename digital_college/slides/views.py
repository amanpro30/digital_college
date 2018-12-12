from django.shortcuts import render, get_object_or_404, redirect
from .models import assign, assign_solution
import os
from django.http import HttpResponse, Http404
from .forms import add_assign, add_assign_solution
from users.models import Courses


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


def assignView(request, class_name, id=None):
    instance = assign_solution.objects.get(id=id)
    file_path = instance.file.url
    file_path = file_path[1:]
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def addSlides(request, class_name):
    course_instance = Courses.objects.get(course_name=class_name)
    slides_files = assign.objects.filter(ass_type='slides')
    form = add_assign(request.POST or None, request.FILES or None)
    if form.is_valid():
        newAssign = form.save(commit=False)
        newAssign.course_id = course_instance
        newAssign.ass_type = 'slides'
        newAssign.save()
    context = {
        "form": form,
        "slides_files": slides_files,
        "class_name": class_name,
    }
    return render(request, 'slides/slides.html', context)


def addAssign(request, class_name):
    username = request.user
    last_assign_file = assign.objects.filter(ass_type='assign').last()
    assign_solution_files = assign_solution.objects.filter(assignment_id=last_assign_file)
    assign_solution_form = add_assign_solution(request.POST, request.FILES)
    if request.method == 'POST':
        form = add_assign(request.POST, request.FILES)
        assign_solution_form = add_assign_solution(request.POST, request.FILES)
        course_instance = Courses.objects.get(course_name=class_name)
        if form.is_valid():
            newAssign = form.save(commit=False)
            newAssign.course_id = course_instance
            newAssign.ass_type = 'assign'
            newAssign.save()
        print(assign_solution_form.is_valid())
        print(assign_solution_form.errors)
        if assign_solution_form.is_valid():
            newAssign = assign_solution_form.save(commit=False)
            newAssign.assignment_id = last_assign_file
            newAssign.student_id = username.registered_user
            newAssign.save()
    else:
        form = add_assign()
    context = {
        'form': form,
        "last_assign_file": last_assign_file,
        'assign_solution_files': assign_solution_files,
        'class_name': class_name,
        'assign_solution_form': assign_solution_form,
    }
    print('Hi')
    print(context['assign_solution_files'])
    return render(request, 'slides/assignment.html', context)


def delSlides(request, class_name, file_id):
    assign.objects.get(pk=file_id).delete()
    # return redirect ('/classrooms/{k}/slides/addSlides/'.format(k=class_name))
    return redirect('users:after:classroom:slides:addSlides', class_name=class_name)
