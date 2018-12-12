from django.shortcuts import render, redirect
from after_login.forms import ClubForm, CourseForm, EmailForm, UploadFileForm
from users.models import Registered_User, Courses, CourseEnrollment, Registered_College, Clubs, ClubEnrollment, Email, \
    UploadedFiles

whos_logged = {
    'F': [('Classrooms', 'format_list_bulleted', 'after:after_login'),
          ('Calendar', 'date_range', 'after:calendarapp:index'),
          ('Profile', 'person', 'after:profile')],
    'S': [('Classrooms', 'format_list_bulleted', 'after:after_login'),
          ('Calendar', 'date_range', 'after:calendarapp:index'),
          ('Profile', 'person', 'after:profile'), ('Clubs', 'public', 'after:clubs:cl_list')],
    'Ad': [('Courses', 'import_contacts', 'after:after_login'),
           ('Faculty', 'record_voice_over', 'after:faculty'),
           ('Clubs', 'public', 'after:clubs:cl_list'), ('Student', 'group', 'after:students'),
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


def profile(request):
    user = request.user
    role = ''
    profile_info = ''
    try:
        if user.registered_user.role:
            role = user.registered_user.role
            profile_info = Registered_User.objects.get(user=user)
    except Registered_User.DoesNotExist:
        role = 'Ad'
        profile_info = Registered_College.objects.get(user=user)
    print(profile_info)
    context = {
        'whos_logged': whos_logged[role],
        'logged_in': user,
        'profile': profile_info,
    }
    return render(request, 'after_login/profile.html', context)


def faculty(request):
    user = request.user
    error = ''
    if request.method == 'POST':
        uploadform = UploadFileForm(request.POST, request.FILES)
        print(uploadform.is_valid())
        print(uploadform.errors)
        if uploadform.is_valid():
            csv1 = UploadedFiles.objects.create(file=request.FILES['file'])
            try:
                with open(csv1.file.url[1:], encoding="utf-8", mode='r') as csv_file:
                    lines = csv_file.readlines()
                    for i in range(1, len(lines)):
                        Email.objects.create(email=lines[i].strip(), role='F')
                        error = 'yes'
            except:
                error = 'no'
    else:
        uploadform = UploadFileForm()
    if request.method == 'POST':
        emailform = EmailForm(request.POST)
        if emailform.is_valid():
            Email.objects.create(email=emailform.cleaned_data['email'], role='F')
    else:
        emailform = EmailForm()
    facultylist = Registered_User.objects.filter(role='F', college_id=user.registered_college.id)
    context = {
        'fac_list': facultylist,
        'whos_logged': whos_logged['Ad'],
        'logged_in': user,
        'emailform': emailform,
        'uploadform': uploadform,
        'added': error,
    }
    return render(request, 'after_login/faculty.html', context)


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
    user = request.user
    error = ''
    if request.method == 'POST':
        uploadform = UploadFileForm(request.POST, request.FILES)
        if uploadform.is_valid():
            csv1 = UploadedFiles.objects.create(file=request.FILES['file'])
            try:
                with open(csv1.file.url[1:], encoding="utf-8", mode='r') as csv_file:
                    lines = csv_file.readlines()
                    for i in range(1, len(lines)):
                        Email.objects.create(email=lines[i].strip(), role='S')
                        error = 'yes'
            except:
                error = 'no'
    else:
        uploadform = UploadFileForm()
    if request.method == 'POST':
        emailform = EmailForm(request.POST)
        if emailform.is_valid():
            Email.objects.create(email=emailform.cleaned_data['email'], role='S')
    else:
        emailform = EmailForm()
    studentslist = Registered_User.objects.filter(role='S', college_id=user.registered_college.id)
    context = {
        'stu_list': studentslist,
        'whos_logged': whos_logged['Ad'],
        'logged_in': request.user,
        'emailform': emailform,
        'uploadform': uploadform,
        'added': error,
    }
    return render(request, 'after_login/students.html', context)


def new_club(request):
    user = request.user
    if request.method == 'POST':
        clubform = ClubForm(request.POST)
        if clubform.is_valid():
            club_name = clubform.cleaned_data['club_name']
            if Clubs.objects.filter(club_name=club_name):
                context = {
                    'whos_logged': whos_logged['Ad'],
                    'logged_in': user,
                    'clubList': Clubs.objects.all().order_by('-date'),
                    'clubform': clubform,
                    'added': 'no',
                }
                return render(request, 'after_login/clubList.html', context)
            Clubs.objects.create(club_name=club_name,
                                 club_head=clubform.cleaned_data['club_head'],
                                 college_id=Registered_College.objects.get(user=user))
            context = {
                'whos_logged': whos_logged['Ad'],
                'logged_in': user,
                'clubList': Clubs.objects.all().order_by('-date'),
                'clubform': clubform,
                'added': 'yes',
            }
            return render(request, 'after_login/clubList.html', context)
    else:
        clubform = ClubForm()

    context = {
        'whos_logged': whos_logged['Ad'],
        'user': user,
        'clubform': clubform,
    }
    return render(request, 'after_login/club_setup.html', context)


def new_course(request):
    user = request.user
    if request.method == 'POST':
        courseform = CourseForm(request.POST)
        if courseform.is_valid():
            course_name = courseform.cleaned_data['course_name']
            if Courses.objects.filter(course_name=course_name):
                context = {
                    'whos_logged': whos_logged['Ad'],
                    'logged_in': user,
                    'classList': Courses.objects.all(),
                    'courseform': courseform,
                    'added': 'no',
                }
                return render(request, 'after_login/classList.html', context)
            Courses.objects.create(course_name=course_name,
                                   faculty_id=courseform.cleaned_data['faculty_id'],
                                   college_id=Registered_College.objects.get(user=user))
            context = {
                'whos_logged': whos_logged['Ad'],
                'logged_in': user,
                'classList': Courses.objects.all(),
                'courseform': courseform,
                'added': 'yes',
            }
            return render(request, 'after_login/classList.html', context)
    else:
        courseform = CourseForm()

    context = {
        'whos_logged': whos_logged['Ad'],
        'user': user,
        'courseform': courseform,
    }
    return render(request, 'after_login/course_setup.html', context)


def deleteclub(request, club_id):
    Clubs.objects.get(id=club_id).delete()
    return redirect(request.META.get('HTTP_REFERER'))


def deleteclass(request, class_id):
    Courses.objects.get(id=class_id).delete()
    return redirect(request.META.get('HTTP_REFERER'))


def deletestudent(request, stu_id):
    Registered_User.objects.get(id=stu_id).delete()
    return redirect(request.META.get('HTTP_REFERER'))
