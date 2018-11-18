from django.shortcuts import render

from users.models import Registered_User, Courses, CourseEnrollment, Registered_College

whos_logged = {
    'F': [('Classrooms', 'format_list_bulleted', 'after:after_login'),
          ('Progress Report', 'trending_up', 'after:progress_report'), ('Calender', 'date_range', 'after:calender'),
          ('Profile', 'person', 'after:profile')],
    'S': [('Classrooms', 'format_list_bulleted', 'after:after_login'),
          ('Progress Report', 'trending_up', 'after:progress_report'), ('Calender', 'date_range', 'after:calender'),
          ('Profile', 'person', 'after:profile'), ('Clubs', 'public', 'after:clubs')],
    'Ad': [('Courses', 'import_contacts', 'after:after_login'),
           ('faculty', 'record_voice_over', 'after:faculty'),
           ('Clubs', 'public', 'after:clubs'), ('Student', 'group', 'after:students'),
           ('Progress Report', 'trending_up', 'after:progress_report'),
           ('Profile', 'person', 'after:profile')],
}


def after_login(request):
    user = request.user
    role = ''
    try:
        if user.registered_user.role:
            role = user.registered_user.role
    except Registered_User.DoesNotExist:
        role = 'Ad'
    classList = []
    if role == 'F':
        data = Registered_User.objects.get(user=request.user)
        print(data)
        classList = Courses.objects.filter(faculty_id=data)
        print(classList)
    elif role == 'S':
        data = Registered_User.objects.get(user=request.user)
        list_course = CourseEnrollment.objects.filter(student_id=data)
        print(list_course)
        for cl in list_course:
            print(cl.course_id)
            classList.append(cl.course_id)
        print(classList)
    elif role == 'Ad':
        classList = Courses.objects.filter(college_id=Registered_College.objects.get(user=request.user))

    context = {
        'whos_logged': whos_logged[role],
        'logged_in': user,
        'classList': classList,
    }
    return render(request, 'after_login/classList.html', context)


def classroom(request):
    classList = Courses.objects.all()
    context = {
        'logged_in': request.user,
        'classList': classList,
    }
    return render(request, 'after_login/classList.html', context)


def progress_report(request):

    return None


def calender(request):
    return None


def profile(request):
    return render(request, 'after_login/profile.html')


def faculty(request):
    return render(request, 'after_login/faculty.html')


def clubs(request):
    return render(request, 'after_login/clubs.html')


def students(request):
    return render(request, 'after_login/students.html')

