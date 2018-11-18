from django.shortcuts import render
from .forms import announcement_form
from .models import announcements
from users.models import Registered_College
# Create your views here.

def announcement(request):
    college_name=request.user.registered_user.college_id
    college_instance=Registered_College.objects.get(Name_Of_College=college_name)
    if request.method=='POST':
        form=announcement_form(request.POST)
        print(form.is_valid())
        form.save()
        announce=announcements.objects.all()
    else:
        form=announcement_form()
    return render(request,'announcements/announcements.html',{'form':form,'announcements':announce})
