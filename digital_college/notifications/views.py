from django.shortcuts import render,redirect
from .models import Notification
from django.contrib.auth.models import User
# Create your views here.

# def show_notifications(request):
#     user_instance=User.objects.get(username=request.user)
#     all_notif=Notification.objects.filter(User=user_instance,viewed=False)
#     context={
#         'notification':all_notif,
#     }
#     return render(request,'Parent/base.html',context)

def delete_notifications(request,notification_id):
    a=Notification.objects.get(id=notification_id)
    a.viewed=True
    a.save()
    return redirect(request.META.get('HTTP_REFERER'))