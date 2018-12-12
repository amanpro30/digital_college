from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import Course_Forms, Edit_Registered_User_Form, Edit_Registered_College_Form, User_reset_form
from .forms import ResetForm
from .forms import ResetDoneForm
from .models import Registered_User, Courses, Email
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
        forms['User_Creation_Form'] = UserCreationForm(request.POST, request.FILES)
        forms['College_Registration_Form'] = College_Registration_Form(request.POST, request.FILES)
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
                                              State=State,)
            if 'image' in request.FILES:
                image = request.FILES['image']
                current_user.image = request.FILES
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
        print(current_user)
    except(TypeError, ValueError, OverflowError):
        current_user = None
    if current_user is not None and account_activation_token.check_token(current_user, token):
        current_user.is_active = True
        current_user.save()
        login(request, current_user)
        return redirect('/users/User_Home')

    else:
        return render(request,'users/invalid_activation_link.html')
        # return HttpResponse('Activation link is invalid')


def User_Registration(request):
    forms = {}
    if request.method == 'POST':
        forms['User_Creation_Form'] = UserCreationForm(request.POST)
        forms['User_Registration_Form'] = User_Registration_Form(request.POST,request.FILES)
        if forms['User_Registration_Form'].is_valid() and forms['User_Creation_Form'].is_valid():
            email = forms['User_Registration_Form'].cleaned_data.get('email')
            role = forms['User_Registration_Form'].cleaned_data.get('role')
            try:
                obj = Email.objects.get(email=email)
                print(obj.email)
                print(obj.role)
                if role != obj.role:
                    obj = False
                    context = {
                        'message': "Please select correct role",
                        'forms': forms
                    }
                    return render(request, 'users/User_Registration.html', context)
            except:
                obj = False
                context = {
                    'message': "You are not registered by your college. Please contact your college",
                    'forms': forms
                }
                return render(request, 'users/User_Registration.html', context)

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

            college_id = forms['User_Registration_Form'].cleaned_data.get('college_id')

            current_user = Registered_User(user=current_user, email=email, First_Name=first_name, Last_Name=last_name,
                                           role=role, college_id=college_id, )
            if 'image' in request.FILES:
                image = request.FILES['image']
                current_user.image = request.FILES
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
            course = Courses(course_name=course_name, faculty_id=faculty_id, college_id=college_id)
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
    return render(request, 'users/web_home.html')


def website_register(request):
    return render(request, 'users/website_register.html')


def base(request):
    return render(request, 'users/base.html')


def PasswordReset(request):
    if request.method == 'POST':
        forms = ResetForm(request.POST)
        if forms.is_valid():
            email = forms.cleaned_data.get('enter_email')
            try:
                current_user = User.objects.get(email=email)
            except:
                current_user = False
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
                return render(request, 'users/password_reset_done.html')
            else:
                context = {
                    'forms': forms,
                    'message': "This e-mail does not exist",
                }
                return render(request, 'users/password_reset_form.html', context)
                # return HttpResponse('Email does not exist')
        else:
            context = {
                'forms': forms,
            }
            return render(request, 'users/password_reset_form.html', context)
    else:
        forms = ResetForm()
        return render(request, 'users/password_reset_form.html', {'forms': forms})


def reset(request, uidb64, token):
    if request.method == 'POST':
        forms = User_reset_form(request.POST)
        if forms.is_valid():
            password1 = forms.cleaned_data.get('Password')
            password2 = forms.cleaned_data.get('Confirm_Password')
            if password1 == password2:
                try:
                    uid = urlsafe_base64_decode(uidb64).decode()
                    current_user = User.objects.get(pk=uid)
                    print(current_user)
                except(TypeError, ValueError, OverflowError):
                    current_user = None
                if current_user is not None and account_activation_token.check_token(current_user, token):
                    current_user.set_password(password1)
                    current_user.save()
                    return HttpResponse('Changed')
                else:
                    context = {
                        'forms': forms,
                        'message': "This link is invalid now"
                    }
                    return render(request, 'users/Reset_done.html', context)
                    # return HttpResponse('Invalid reset link')
            else:
                context = {
                    'forms': forms,
                    'message': "Your password does't match"
                }
                return render(request, 'users/Reset_done.html', context)
                # return HttpResponse('Password does not match')
        else:
            return render(request, 'users/Reset_done.html', {'forms': forms})
    else:
        forms = User_reset_form()
        return render(request, 'users/Reset_done.html', {'forms': forms})


def reset2(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        current_user = User.objects.get(pk=uid)
        print(current_user)
    except(TypeError, ValueError, OverflowError):
        current_user = None
    if current_user is not None and account_activation_token.check_token(current_user, token):
        if request.method == 'POST':
            forms = ResetDoneForm(request.POST)
            if forms.is_valid():
                password1 = forms.cleaned_data.get('Password')
                password2 = forms.cleaned_data.get('Confirm_Password')
                if password1 == password2:
                    current_user.set_password(password1)
                    current_user.save()
                    login(request, current_user)
                    return redirect('/users/User_Home')
                    # return HttpResponse('Changed')
                else:
                    context={
                        'forms': forms,
                        'message': "Your password does't match"
                    }
                    return render(request, 'users/Reset_done.html', context)
            else:
                return render(request, 'users/Reset_done.html', {'forms': forms})
        else:
            forms = ResetDoneForm()
            return render(request, 'users/Reset_done.html', {'forms': forms})
        current_user.set_password(password1)
        current_user.save()
        return HttpResponse('Changed')
    else:
        return render(request, 'users/invalid_reset_link.html')
        # return HttpResponse('Invalid reset link')


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


@login_required()
def profile_update(request):
    if request.method == 'POST':
        forms = Edit_Registered_User_Form(request.POST, instance=request.user.registered_user)
        if forms.is_valid():
            forms.save()
            return HttpResponse('Edited')
    else:
        forms = Edit_Registered_User_Form(instance=request.user.registered_user)
        args = {'forms': forms}
        return render(request, 'users/editprofile.html', args)


@login_required()
def profile_update2(request):
    if request.method == 'POST':
        forms = Edit_Registered_College_Form(request.POST, instance=request.user.registered_college)
        if forms.is_valid():
            forms.save()
            return HttpResponse('Edited')
    else:
        forms = Edit_Registered_College_Form(instance=request.user.registered_college)
        args = {'forms': forms}
        return render(request, 'users/editprofile.html', args)



def progress_report(request):
    return None


def calender(request):
    return None


def profile(request):
   return render(request,'users/base.html')

