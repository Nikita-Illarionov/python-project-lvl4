from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TasksForm
from django.views.generic import UpdateView, DeleteView, ListView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .filters import TasksFilter



class TasksList(LoginRequiredMixin, ListView):
    model = Tasks
    template_name = "tasks/tasks.html"
    context_object_name = 'tasks'
    login_url = 'login'

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



class CreateTask(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Task create view."""

    model = Tasks
    fields = ['name', 'description', 'status', 'assigned_to', 'labels']
    template_name = 'tasks/create.html'
    success_url = '/tasks/'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)



class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Tasks
    template_name = 'tasks/update.html'
    form_class = TasksForm
    login_url = 'login'



class DeleteTask(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tasks
    template_name = 'tasks/delete.html'
    success_url = '/tasks/'
    login_url = 'tasks'

    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user

    def handle_no_permission(self):
        return redirect(self.login_url)
