from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.db.models import Q

# Create your views here.
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)

    # Get filter and search parameters
    status_filter = request.GET.get("status")
    deadline_filter = request.GET.get("deadline")
    search_query = request.GET.get("search")

    if status_filter:
        tasks = tasks.filter(status=status_filter)
    
    if deadline_filter:
        tasks = tasks.filter(deadline=deadline_filter)

    if search_query:
        tasks = tasks.filter(title__icontains=search_query)

    return render(request, "tasks/task_list.html", {
        "tasks": tasks,
        "status_filter": status_filter,
        "deadline_filter": deadline_filter,
        "search_query": search_query
    })

@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("task_list")
    else:
        form = TaskForm()

    return render(request, "tasks/create_task.html", {"form": form})

@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    
    return render(request, "tasks/update_task.html", {"form": form})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    
    return render(request, "tasks/delete_task.html", {"task": task})