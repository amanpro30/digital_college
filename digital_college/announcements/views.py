from django.shortcuts import render
from .forms import announcement_form
# Create your views here.

def announcement(request):
    if request.method=='POST':
        form=announcement_form(request.POST)
        print(form.is_valid())

    else:
        form=announcement_form()
    return render(request,'announcements/announcements.html',{'form':form})