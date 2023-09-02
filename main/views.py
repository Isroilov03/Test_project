from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def index_view(request):
    context = {
        'todo' : Todo.objects.all()
    }
    return  render(request, 'index.html', context)


def create_task_view(request):
    if request.method == "POST":
        task = request.POST['task']
        Todo.objects.create(
            task=task
        )
        return redirect('index_url')
    return render(request, 'index.html')

def delete_task_view(request, pk):
    task = Todo.objects.get(pk=pk)
    task.status = 'Deleted'
    task.save()
    return redirect('index_url')


def update_status_view(request, pk):
    task = Todo.objects.get(pk=pk)
    task.status = 'Finished'
    task.save()
    return redirect('index_url')


def deleted_view(request):
    status = 'Deleted'
    context = {
        'deleted' : Todo.objects.filter(status=status)
    }
    return render(request, 'delete.html', context)


def finished_view(request):
    status ='Finished'
    context = {
        'finished' : Todo.objects.filter(status=status)
    }
    return render(request, 'finished.html', context)


def in_progress_view(request):
    status = 'In Progress'
    context = {
        'in_progress' : Todo.objects.filter(status=status)
    }
    return render(request, 'inprogress.html', context)