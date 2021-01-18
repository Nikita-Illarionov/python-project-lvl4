from django.shortcuts import render, redirect
from .models import Tasks, Statuses, Tags
from .forms import StatusesForm, TagsForm
from django.views.generic import UpdateView, DeleteView


def index(request):
    tasks = Tasks.objects.all()
    return render(request, 'task_manager/index.html', {'tasks': tasks})



def status_page(request):
    statuses = Statuses.objects.all()
    return render(request, 'tasks/statuses.html', {'statuses': statuses})


def tag_page(request):
    tags = Tags.objects.all()
    return render(request, 'tasks/tags.html', {'tags': tags})



def create_status(request):
    error = ''
    if request.method == 'POST':
        form = StatusesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('statuses')
        else:
            error = 'Форма заполнена неверно'


    form = StatusesForm()
    data = {'form': form, 'error': error}
    return render(request, 'tasks/create_status.html', data)



class StatusUpdateView(UpdateView):
    model = Statuses
    template_name = 'tasks/create_status.html'
    field = ['name']

    form_class = StatusesForm




class StatusDeleteView(DeleteView):
    model = Statuses
    template_name = 'tasks/delete_status.html'
    field = ['name']
    success_url = '/statuses/'



def create_tag(request):
    error = ''
    if request.method == 'POST':
        form = TagsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tags')
        else:
            error = 'Форма заполнена неверно'


    form = TagsForm()
    data = {'form': form, 'error': error}
    return render(request, 'tasks/create_tag.html', data)



class TagUpdateView(UpdateView):
    model = Tags
    template_name = 'tasks/create_tag.html'
    field = ['name']

    form_class = TagsForm




class TagDeleteView(DeleteView):
    model = Tags
    template_name = 'tasks/delete_tag.html'
    field = ['name']
    success_url = '/tags/'
