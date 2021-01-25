from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TasksForm
from django.views.generic import UpdateView, DeleteView, ListView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .filters import TasksFilter
from django.contrib import messages
from django.utils.translation import ugettext as _



class TasksList(LoginRequiredMixin, ListView):
    model = Tasks
    template_name = "tasks/main.html"
    context_object_name = 'tasks'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('NotLoginStatus'))
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

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
    success_message = 'Задача успешно создана'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('NotLoginStatus'))
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)



class UpdateTask(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Tasks
    template_name = 'tasks/update.html'
    form_class = TasksForm
    login_url = 'login'
    success_message = 'Задача успешно обновлена'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('NotLoginStatus'))
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)




class DeleteTask(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Tasks
    template_name = 'tasks/delete.html'
    success_url = '/tasks/'
    login_url = 'tasks'
    success_message = 'Задача успешно удалена'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('NotLoginStatus'))
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        obj = self.get_object()
        user_is_creator = obj.creator == self.request.user
        if not user_is_creator:
            messages.error(self.request, _('CannotDeleteTask'))
        return user_is_creator

    def handle_no_permission(self):
        return redirect(self.login_url)

    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteTask, self).delete(request, *args, **kwargs)

