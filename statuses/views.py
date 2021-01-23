from .models import Statuses
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import StatusForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin



class StatusView(LoginRequiredMixin, ListView):
    model = Statuses
    template_name = "statuses/main.html"
    context_object_name = 'statuses'
    form_class = StatusForm
    login_url = 'login'



class CreateStatus(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Task create view."""

    model = Statuses
    form_class = StatusForm
    template_name = 'statuses/create.html'
    success_url = '/statuses/'
    login_url = 'login'
    success_message = 'Статус успешно создан'



class UpdateStatus(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Statuses
    success_message = 'Статус успешно изменён'
    template_name = 'statuses/update.html'
    form_class = StatusForm
    login_url = 'login'



class DeleteStatus(LoginRequiredMixin, DeleteView):
    model = Statuses
    template_name = 'statuses/delete.html'
    field = ['name']
    success_url = '/statuses/'
    login_url = 'tasks'
    error_url = '/statuses/'

    def get_error_url(self):
        if self.error_url:
            return self.error_url.format(**self.object.__dict__)
        else:
            raise ImproperlyConfigured(
               "No error URL to redirect to. Provide a error_url.")

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect. 
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        error_url = self.get_error_url()
        try:
             self.object.delete()
             messages.success(request, 'Статус успешно удалён')
             return HttpResponseRedirect(success_url)
        except models.ProtectedError:
             return HttpResponseRedirect(error_url)
