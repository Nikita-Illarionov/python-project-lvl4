from django.shortcuts import render, redirect
from .models import Labels
from .forms import LabelForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class LabelView(LoginRequiredMixin, ListView):
    model = Labels
    template_name = "labels/main.html"
    context_object_name = 'labels'
    login_url = 'login'



class CreateLabel(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Task create view."""

    model = Labels
    form_class = LabelForm
    template_name = 'labels/create.html'
    success_url = '/labels/'
    login_url = 'login'
    success_message = 'Метка успешно создана'




class UpdateLabel(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Labels
    template_name = 'labels/update.html'
    form_class = LabelForm
    login_url = 'login'
    success_message = 'Метка успешно обновлена'




class DeleteLabel(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Labels
    template_name = 'labels/delete.html'
    success_url = '/labels/'
    context_object_name = 'labels'
    login_url = 'login'
    success_message = 'Метка успешно удалена'
    error_url = '/statuses/'

    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteLabel, self).delete(request, *args, **kwargs)
