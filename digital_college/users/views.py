from django.shortcuts import render
from django.shortcuts import redirect
from .forms import User_Registration_Form
from .forms import College_Registration_Form
from .models import Registered_User
from .models import Registered_College
from django.contrib.auth.forms import UserCreationForm


def User_Home(request):
    classrooms = ['cs1', 'cs2', 'cs3']
    clubs = ['cb1', 'cb2', 'cb3']
    context = {
        'classrooms': classrooms,
        'clubs': clubs
    }
    return render(request, 'users/../templates/after_login/main.html', context)


def College_Home(request):
    return render(request, 'users/college_home.html')


def College_Registration(request):
    forms = {}
    if request.method == 'POST':
        forms['User_Creation_Form'] = UserCreationForm(request.POST)
        forms['College_Registration_Form'] = College_Registration_Form(request.POST)
        if forms['College_Registration_Form'].is_valid() and forms['User_Creation_Form'].is_valid():
            current_user = forms['User_Creation_Form'].save(commit=False)
            current_user.save()
            Name_Of_College = forms['College_Registration_Form'].cleaned_data.get('Name_Of_College')
            email = forms['College_Registration_Form'].cleaned_data.get('email')
            College_Registration_Number = forms['College_Registration_Form'].cleaned_data.get(
                'College_Registration_Number')
            City = forms['College_Registration_Form'].cleaned_data.get('City')
            State = forms['College_Registration_Form'].cleaned_data.get('State')
            current_user = Registered_College(user=current_user, Name_Of_College=Name_Of_College, email=email,
                                              College_Registration_Number=College_Registration_Number, City=City,
                                              State=State)
            current_user.save()
            return redirect('College_Home')
    else:
        forms['User_Creation_Form'] = UserCreationForm()
        forms['College_Registration_Form'] = College_Registration_Form()
    return render(request, 'users/College_Registration.html', {'forms': forms})


def User_Registration(request):
    forms = {}
    if request.method == 'POST':
        forms['User_Creation_Form'] = UserCreationForm(request.POST)
        forms['User_Registration_Form'] = User_Registration_Form(request.POST)
        if forms['User_Registration_Form'].is_valid() and forms['User_Creation_Form'].is_valid():
            first_name = forms['User_Registration_Form'].cleaned_data.get('first_name')
            last_name = forms['User_Registration_Form'].cleaned_data.get('last_name')
            email = forms['User_Registration_Form'].cleaned_data.get('email')
            role = forms['User_Registration_Form'].cleaned_data.get('role')
            college_id = forms['User_Registration_Form'].cleaned_data.get('college_id')
            generated_key = 123
            activation_key = forms['User_Registration_Form'].cleaned_data.get('activation_key')
            current_user = forms['User_Creation_Form'].save(commit=False)
            current_user.save()
            current_user = Registered_User(user=current_user, fisrt_name=first_name, last_name=last_name, email=email, role=role, college_id=college_id,activation_key=activation_key)
            current_user.save()
            return redirect('User_Home')
            # return redirect('User_Registration')
    else:
        forms['User_Creation_Form'] = UserCreationForm()
        forms['User_Registration_Form'] = User_Registration_Form()
    return render(request, 'users/User_Registration.html', {'forms': forms})


def website_homepage(request):
    return render(request, 'users/website_homepage.html')


def website_register(request):
    return render(request, 'users/website_register.html')


def base(request):
    return render(request, 'users/base.html')


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
    return render(request, 'users/../templates/after_login/main.html', context)


def progress_report(request):
    return None


def calender(request):
    return None


def profile(request):
    return None
