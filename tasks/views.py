from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TasksForm
from django.views.generic import UpdateView, DeleteView, ListView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .filters import TasksFilter



class TasksList(ListView):
    model = Tasks
    template_name = "tasks/tasks.html"
    context_object_name = 'tasks'

    def get_queryset(self):
        """Filter by tag if it is provided in GET parameters."""
        queryset = Tasks.objects.all().order_by('-pk')
        if self.request.GET.get('tasks'):
            queryset = queryset.filter(tags__name=self.request.GET.get('tasks'))
        return queryset

    def get_context_data(self, **kwargs):
        """Get filtered data if it's provided by requests."""
        context = super().get_context_data(**kwargs)
        context['filter'] = TasksFilter(
            self.request.GET,
            queryset=self.get_queryset(),
        )
        return context



class CreateTask(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """Task create view."""

    model = Tasks
    fields = ['name', 'description', 'status', 'assigned_to']
    template_name = 'tasks/create.html'
    success_url = '/tasks/'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


'''
def create_task(request):
    error = ''
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        else:
            error = 'Форма заполнена неверно'

    form = TasksForm()
    data = {'form': form, 'error': error}
    return render(request, 'tasks/create.html', data)

'''

class UpdateTask(UpdateView):
    model = Tasks
    template_name = 'tasks/update.html'
    form_class = TasksForm



class DeleteTask(DeleteView):
    model = Tasks
    template_name = 'tasks/delete.html'
    success_url = '/tasks/'
