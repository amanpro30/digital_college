from django.shortcuts import render, redirect

from users.forms import ExamForm
from users.models import Registered_User, Courses, CourseEnrollment, Exam


def class_home(request, class_name):
    return render(request, 'quiz/base_classrooms.html', {'class_name': class_name}, {'class_name': class_name})


def members(request, class_name):
    user = request.user
    course_id = Courses.objects.get(course_name=class_name)
    faculty = course_id.faculty_id
    students = CourseEnrollment.objects.filter(course_id=course_id)
    context = {
        'class_name': class_name,
        'faculty': faculty,
        'students': students,
        'user': user
    }
    return render(request, 'after_login/members.html', context)


def remStudent(request, class_name, user_id):
    course_id = Courses.objects.get(course_name=class_name)
    CourseEnrollment.objects.get(student_id=Registered_User.objects.get(id=user_id), course_id=course_id).delete()
    return redirect(request.META.get('HTTP_REFERER'), class_name)


def addStudents(request, class_name):
    user = request.user
    course_id = Courses.objects.get(course_name=class_name, college_id=user.registered_college.id)
    coursestuds = CourseEnrollment.objects.filter(course_id=course_id)
    list_of_student_in_course = []
    for st in coursestuds:
        list_of_student_in_course.append(st.student_id.id)
    print(list_of_student_in_course)
    students = Registered_User.objects.filter(role='S', college_id=user.registered_college.id)
    student_list = []
    for stud in students:
        if stud.id not in list_of_student_in_course:
            student_list.append(stud)
    print(student_list)
    context = {
        'class_name': class_name,
        'Students': student_list,
        'user': user,
    }
    return render(request, 'after_login/addStudents.html', context)


def addStud(request, class_name, stud_id):
    user = request.user
    course_id = Courses.objects.get(course_name=class_name, college_id=user.registered_college.id)
    CourseEnrollment.objects.create(student_id=Registered_User.objects.get(id=stud_id), course_id=course_id)
    return redirect(request.META.get('HTTP_REFERER'), class_name)
