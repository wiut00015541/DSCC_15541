from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from .models import Task
from django.contrib.auth.decorators import login_required


@login_required
def task_list(request):
    tasks = Task.objects.filter(owner=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})