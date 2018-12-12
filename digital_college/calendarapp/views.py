from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

from users.models import Registered_User
from .models import Entry
from .forms import Entryform, EntryUpdateForm
from after_login import views as after_helper

# Create your views here.

whos_logged = after_helper.whos_logged


def index(request):
    user = request.user
    role = user.registered_user.role
    entries = Entry.objects.filter(userId=Registered_User.objects.get(user=user)).order_by('-date')
    context = {
        'whos_logged': whos_logged[role],
        'logged_in': user,
        'entries': entries
    }
    return render(request, 'calendarapp/index.html', context)


def details(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    return render(request, 'calendarapp/details.html', {'entry': entry})


def add(request):
    if request.method == 'POST':
        form = Entryform(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']

            Entry.objects.create(
                userId=Registered_User.objects.get(user=request.user),
                name=name,
                date=date,
                description=description,
            ).save()
            user = request.user
            role = user.registered_user.role
            entries = Entry.objects.filter(userId=Registered_User.objects.get(user=user)).order_by('-date')
            context = {
                'whos_logged': whos_logged[role],
                'logged_in': user,
                'entries': entries
            }
            return render(request, 'calendarapp/index.html', context)
    else:
        form = Entryform()
    user = request.user
    role = user.registered_user.role
    context = {
        'whos_logged': whos_logged[role],
        'logged_in': user,
        'form': form,
    }
    return render(request, 'calendarapp/form.html', context)


def delete(request, entry_id):
    # if request.method == 'DELETE':
    #     entry = get_object_or_404(Entry, pk=pk)
    #     entry.delete()
    #
    # return HttpResponseRedirect("/")
    entry = Entry.objects.get(id=entry_id)
    entry.delete()
    return redirect('after:calendarapp:index')


def edit(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    user = request.user
    role = user.registered_user.role
    # entry = Entry.objects.filter(userId=Registered_User.objects.get(user=user)).order_by('-date')
    if request.method == 'POST':
        form = EntryUpdateForm(request.POST, instance=entry)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.save()
            return redirect('after:calendarapp:index')
    else:
        form = EntryUpdateForm(instance=entry)
        # template = 'calendarapp/form.html'
        template = 'calendarapp/edit.html'
        context = {
            'whos_logged': whos_logged[role],
            'logged_in': user,
            'form': form,
        }
        return render(request, template, context)
