from django.shortcuts import render,HttpResponse
from django.shortcuts import redirect
from .forms import User_Registration_Form
from .forms import College_Registration_Form
from .models import Registered_User
from .models import Registered_College
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string, get_template
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .token import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
import socket
from django.contrib.auth.models import User


def User_Home(request):
    classrooms=['cs1', 'cs2', 'cs3']
    clubs=['cb1', 'cb2', 'cb3']
    context = {
        'classrooms': classrooms,
        'clubs': clubs
    }
    return render(request,'users/user_home.html', context)

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
            College_Registration_Number = forms['College_Registration_Form'].cleaned_data.get('College_Registration_Number')
            City = forms['College_Registration_Form'].cleaned_data.get('City')
            State = forms['College_Registration_Form'].cleaned_data.get('State')
            current_user = Registered_College(user=current_user, Name_Of_College=Name_Of_College, email=email,
                                              College_Registration_Number=College_Registration_Number, City=City, State=State)

            current_user.is_active = False
            current_user.save()
            socket.getaddrinfo('localhost', 8080)
            current_site = get_current_site(request)
            mail_subject = 'digital college account'
            message = render_to_string('users/activate_email.html',{
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
            return HttpResponse('Please confirm your email address to complete the registration')
            # return redirect('College_Home')
    else:
        forms['User_Creation_Form'] = UserCreationForm()
        forms['College_Registration_Form'] = College_Registration_Form()
    return render(request, 'users/College_Registration.html', {'forms': forms})

def activate(request, uidb64, token):
    try:
        uid =urlsafe_base64_decode(uidb64).decode()
        current_user = User.objects.get(pk=uid)
        print("ravish")
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
            current_user = forms['User_Creation_Form'].save(commit=False)
            current_user.save()
            email = forms['User_Registration_Form'].cleaned_data.get('email')
            role = forms['User_Registration_Form'].cleaned_data.get('role')
            college_id = forms['User_Registration_Form'].cleaned_data.get('college_id')
            activation_key = forms['User_Registration_Form'].cleaned_data.get('activation_key')
            current_user = Registered_User(user=current_user, email=email, role=role, college_id=college_id,
                                           activation_key=activation_key)
            current_user.save()
            return redirect('User_Home')
    else:
        forms['User_Creation_Form'] = UserCreationForm()
        forms['User_Registration_Form'] = User_Registration_Form()
    return render(request, 'users/User_Registration.html', {'forms': forms})




def website_homepage(request):
    return render(request,'users/website_homepage.html')

def website_register(request):
    return render(request,'users/website_register.html')

def base(request):
    return render(request,'users/base.html')
