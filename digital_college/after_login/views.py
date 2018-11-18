from django.shortcuts import render

from users.models import Registered_User, Courses, CourseEnrollment, Registered_College, Clubs, ClubEnrollment

whos_logged = {
    'F': [('Classrooms', 'format_list_bulleted', 'after:after_login'),
          ('Progress Report', 'trending_up', 'after:progress_report'), ('Calendar', 'date_range', 'after:calendarapp:index'),
          ('Profile', 'person', 'after:profile')],
    'S': [('Classrooms', 'format_list_bulleted', 'after:after_login'),
          ('Progress Report', 'trending_up', 'after:progress_report'), ('Calendar', 'date_range', 'after:calendarapp:index'),
          ('Profile', 'person', 'after:profile'), ('Clubs', 'public', 'after:clubs:cl_list')],
    'Ad': [('Courses', 'import_contacts', 'after:after_login'),
           ('faculty', 'record_voice_over', 'after:faculty'),
           ('Clubs', 'public', 'after:clubs:cl_list'), ('Student', 'group', 'after:students'),
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


def progress_report(request):
    return None


def calender(request):
    return None


def profile(request):
    return render(request, 'after_login/profile.html')


def faculty(request):
    return render(request, 'after_login/faculty.html')


def clubs(request):
    print('hello1')
    user = request.user
    role = ''
    try:
        if user.registered_user.role:
            role = user.registered_user.role
    except Registered_User.DoesNotExist:
        role = 'Ad'
    clubList = []
    if role == 'S':
        data = Registered_User.objects.get(user=request.user)
        list_clubs = ClubEnrollment.objects.filter(student_id=data)
        print(list_clubs)
        for cl in list_clubs:
            print(cl.club_id)
            clubList.append(cl.club_id)
        print(clubList)
    elif role == 'Ad':
        clubList = Clubs.objects.filter(college_id=Registered_College.objects.get(user=request.user))

    context = {
        'whos_logged': whos_logged[role],
        'logged_in': user,
        'clubList': clubList,
    }
    return render(request, 'after_login/clubList.html', context)


def students(request):
    return render(request, 'after_login/students.html')

