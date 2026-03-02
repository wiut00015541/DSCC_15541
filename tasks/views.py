from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from django.shortcuts import get_object_or_404


@login_required
def task_list(request):
    active_tasks = Task.objects.filter(owner=request.user, status='active')
    completed_tasks = Task.objects.filter(owner=request.user, status='completed')
    cancelled_tasks = Task.objects.filter(owner=request.user, status='cancelled')

    return render(request, 'task_list.html', {
        'active_tasks': active_tasks,
        'completed_tasks': completed_tasks,
        'cancelled_tasks': cancelled_tasks
    })

@login_required
def change_status(request, pk, new_status):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    task.status = new_status
    task.save()
    return redirect('task_list')


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

@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            form.save_m2m()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'task_form.html', {'form': form})

@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'task_form.html', {'form': form})

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)

    if request.method == "POST":
        task.delete()
        return redirect('task_list')

    return render(request, 'task_confirm_delete.html', {'task': task})