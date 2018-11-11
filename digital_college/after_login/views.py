from django.shortcuts import render

whos_logged = {
    'F': {'classrooms', 'Progress Report', 'Calender', 'profile'},
    'S': {'classroom', 'Progress Report', 'Calender', 'clubs', 'profile'},
    'Ad': {'classroom', 'courses', 'faculty', 'clubs', 'Progress Report', 'Profile'},
}


def after_login(request):
    user = request.user
    role = 'Ad'
    if user.registered_user.role:
        role = user.registered_user.role
    context = {
        'whos_logged': role,
    }
    return render(request, 'after_login/main.html', context)


def progress_report(request):
    return None


def calender(request):
    return None


def profile(request):
    return None
