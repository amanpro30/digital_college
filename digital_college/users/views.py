from .forms import Course_Forms
from .forms import ResetForm
from .forms import ResetDoneForm
from .models import Registered_User, Courses
from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from .forms import User_Registration_Form, College_Registration_Form
from .models import Registered_College
from django.contrib.auth.forms import UserCreationForm
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from .token import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
import socket
from django.contrib.auth.models import User


def College_Home(request):
    return render(request, 'users/college_home.html')


def College_Registration(request):
    forms = {}
    if request.method == 'POST':
        forms['User_Creation_Form'] = UserCreationForm(request.POST)
        forms['College_Registration_Form'] = College_Registration_Form(request.POST)
        if forms['College_Registration_Form'].is_valid() and forms['User_Creation_Form'].is_valid():
            current_user = forms['User_Creation_Form'].save(commit=False)
            username = forms['User_Creation_Form'].cleaned_data.get('username')
            email = forms['College_Registration_Form'].cleaned_data.get('email')
            password = forms['User_Creation_Form'].cleaned_data.get('password1')
            current_user = User(username=username, email=email)
            current_user.set_password(password)
            current_user.is_active = False
            current_user.save()
            current_site = get_current_site(request)
            mail_subject = 'digital college account'

            message = render_to_string('users/activate_email.html', {
                'current_user': current_user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(current_user.pk)).decode(),
                'token': account_activation_token.make_token(current_user),
            })
            to_email = forms['College_Registration_Form'].cleaned_data.get('email')
            email = EmailMessage(
                    mail_subject, message, to=[to_email]
            )
            email.send()
            Name_Of_College = forms['College_Registration_Form'].cleaned_data.get('Name_Of_College')
            email = forms['College_Registration_Form'].cleaned_data.get('email')
            College_Registration_Number = forms['College_Registration_Form'].cleaned_data.get('College_Registration_Number')
            City = forms['College_Registration_Form'].cleaned_data.get('City')
            State = forms['College_Registration_Form'].cleaned_data.get('State')
            current_user = Registered_College(user=current_user, Name_Of_College=Name_Of_College, email=email,
                                              College_Registration_Number=College_Registration_Number, City=City,
                                              State=State)
            current_user.save()
            return render(request, 'users/email_verification.html')

    else:
        forms['User_Creation_Form'] = UserCreationForm()
        forms['College_Registration_Form'] = College_Registration_Form()
    return render(request, 'users/College_Registration.html', {'forms': forms})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        current_user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError):
        current_user = None
    if current_user is not None and account_activation_token.check_token(current_user, token):
        current_user.is_active = True
        current_user.save()
        return redirect('/users/User_Home')

    else:
        return HttpResponse('Activation link is invalid')


def User_Registration(request):
    forms = {}
    if request.method == 'POST':
        forms['User_Creation_Form'] = UserCreationForm(request.POST)
        forms['User_Registration_Form'] = User_Registration_Form(request.POST)
        if forms['User_Registration_Form'].is_valid() and forms['User_Creation_Form'].is_valid():
            email = forms['User_Registration_Form'].cleaned_data.get('email')
            username = forms['User_Creation_Form'].cleaned_data.get('username')
            password = forms['User_Creation_Form'].cleaned_data.get('password1')
            current_user = User(username=username, email=email)
            current_user.set_password(password)
            current_user.is_active = False
            current_user.save()
            current_site = get_current_site(request)
            mail_subject = 'digital college account'
            message = render_to_string('users/activate_email.html', {
                'current_user': current_user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(current_user.pk)).decode(),
                'token': account_activation_token.make_token(current_user),
            })
            to_email = forms['User_Registration_Form'].cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            first_name = forms['User_Registration_Form'].cleaned_data.get('First_Name')
            last_name = forms['User_Registration_Form'].cleaned_data.get('Last_Name')
            role = forms['User_Registration_Form'].cleaned_data.get('role')
            college_id = forms['User_Registration_Form'].cleaned_data.get('college_id')
            current_user = Registered_User(user=current_user, email=email, First_Name=first_name, Last_Name=last_name,
                                           role=role, college_id=college_id,)
            current_user.save()
            return render(request, 'users/email_verification.html')

    else:
        forms['User_Creation_Form'] = UserCreationForm()
        forms['User_Registration_Form'] = User_Registration_Form()
    return render(request, 'users/User_Registration.html', {'forms': forms})

def add_courses(request):
    if request.method == 'POST':
        forms = Course_Forms(request.POST)
        if forms.is_valid():
            course_name = forms.cleaned_data.get('course_name')
            faculty_id = forms.cleaned_data.get('faculty_id')
            college_id = forms.cleaned_data.get('college_id')
            course = Courses(course_name=course_name, faculty_id=faculty_id,college_id=college_id)
            course.save()
            return HttpResponse('Course Added')
            # return redirect('/users/User_Home/')
        else:
            forms = Course_Forms()
            return render(request, 'users/Add_Course.html', {'forms': forms})
    else:
        forms = Course_Forms()
        return render(request, 'users/Add_Course.html', {'forms': forms})

def website_homepage(request):
    return render(request, 'users/website_homepage.html')


def website_register(request):
    return render(request, 'users/website_register.html')


def base(request):
    return render(request, 'users/base.html')


def PasswordReset(request):
    if request.method == 'POST':
        forms = ResetForm(request.POST)
        if forms.is_valid():
            email = forms.cleaned_data.get('enter_email')
            current_user = User.objects.get(email=email)
            if current_user:
                socket.getaddrinfo('localhost', 8080)
                current_site = get_current_site(request)
                mail_subject = 'Reset Your Password'
                message = render_to_string('users/password_reset_email.html', {
                    'current_user': current_user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(current_user.pk)).decode(),
                    'token': account_activation_token.make_token(current_user),
                })
                to_email = forms.cleaned_data.get('enter_email')
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                # message = "Please confirm your email address to complete the registration"
                # return HttpResponse('Please confirm your email address to complete the registration')
                return render(request, 'users/password_reset_done.html')
            else:
                return HttpResponse('Email does not exist')
        else:
            return HttpResponse('Please enter a valid email')
    else:
        forms = ResetForm()
        return render(request, 'users/password_reset_form.html', {'forms': forms})


def reset(request, uidb64, token):
    if request.method == 'POST':
        forms = ResetDoneForm(request.POST)
        if forms.is_valid():
            password1 = forms.cleaned_data.get('Password')
            password2 = forms.cleaned_data.get('Confirm_Password')
            if password1 == password2:
                try:
                    uid = urlsafe_base64_decode(uidb64).decode()
                    current_user = User.objects.get(pk=uid)
                except(TypeError, ValueError, OverflowError):
                    current_user = None
                if current_user is not None and account_activation_token.check_token(current_user, token):
                    current_user.set_password(password1)
                    current_user.save()
                    return HttpResponse('Changed')
                else:
                    return HttpResponse('Invalid reset link')
            else:
                return HttpResponse('Password does not match')
        else:
            return render(request, 'users/Reset_done.html', {'forms': forms})
    else:
        forms = ResetDoneForm()
        return render(request, 'users/Reset_done.html', {'forms': forms})

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
   return render(request,'users/base.html')

