from django.shortcuts import render
from tasks.models import Tasks


def index(request):
    tasks = Tasks.objects.all()
    return render(request, 'task_manager/index.html', {'tasks': tasks})
