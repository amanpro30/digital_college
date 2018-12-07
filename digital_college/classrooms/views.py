from django.shortcuts import render
from users.models import Registered_User, Courses, CourseEnrollment


# Create your views here.

def class_home(request, class_name):
    return render(request, 'quiz/base_classrooms.html', {'class_name': class_name}, {'class_name': class_name})


def members(request, class_name):
    user = request.user
    course_id = Courses.objects.get(course_name=class_name)
    faculty = course_id.faculty_id
    students = CourseEnrollment.objects.filter(course_id=course_id)
    return render(request, 'after_login/members.html',
                  {'class_name': class_name, 'faculty': faculty, 'students': students, 'user': user})
