from django.shortcuts import render
from django.forms import ModelForm
from .models import Registered_User,Registered_College
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import HttpResponseRedirect,HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm



def User_Registration(request):
    forms={}
    if request.method == 'POST':
        forms['User_Creation_Form']=UserCreationForm(request.POST)
        forms['User_Registration_Form']=User_Registration_Form(request.POST)
        if forms['User_Registration_Form'].is_valid() and forms['User_Creation_Form'].is_valid():
            current_user=forms['User_Creation_Form'].save(commit=False)
            username=forms['User_Creation_Form'].cleaned_data.get('username')
            password=forms['User_Creation_Form'].cleaned_data.get('password1')
            user=current_user
            user.save()
            email=forms['User_Registration_Form'].cleaned_data.get('email')
            role=forms['User_Registration_Form'].cleaned_data.get('role')
            college_id=forms['User_Registration_Form'].cleaned_data.get('college_id')
            activation_key=forms['User_Registration_Form'].cleaned_data.get('activation_key')
            current_user=Registered_User(user=user,email=email,role=role,college_id=college_id,activation_key=activation_key)
            current_user.save()
            return redirect('User_Home')
    else:
        forms['User_Registration_Form'] = User_Registration_Form()
        forms['User_Creation_Form'] = UserCreationForm()
    return render(request,'users/User_Registration.html',{'forms':forms})



def College_Registration(request):
    if request.method == 'POST':
        form =  College_Registration_Form(request.POST)
        if form.is_valid():
            print('hello')
            form.save()
            return redirect('College_Home')
    else:
        form = College_Registration_Form()
    return render(request,'users/College_Registration.html',{'form':form})

def User_Home(request):
    classrooms=['cs1','cs2','cs3']
    clubs=['cb1','cb2','cb3']
    context = {
        'classrooms':classrooms,
        'clubs':clubs
    }
    return render(request,'users/user_home.html',context)

def College_Home(request):
    return render(request,'users/college_home.html')

def website_homepage(request):
    return render(request,'users/website_homepage.html')

def website_register(request):
    return render(request,'users/website_register.html')

def base(request):
    return render(request,'users/base.html')