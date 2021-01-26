from django.shortcuts import render, redirect
from .models import Labels
from .forms import LabelForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.urls import reverse


class LabelView(LoginRequiredMixin, ListView):
    model = Labels
    template_name = "labels/main.html"
    context_object_name = 'labels'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('NotLoginStatus'))
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)



class CreateLabel(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Task create view."""

    model = Labels
    fields = ['name']
    #form_class = LabelForm
    template_name = 'labels/create.html'
    success_url = '/labels/'
    login_url = 'login'
    success_message = 'Метка успешно создана'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('NotLoginStatus'))
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)




class UpdateLabel(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Labels
    template_name = 'labels/update.html'
    form_class = LabelForm
    login_url = 'login'
    success_message = 'Метка успешно изменена'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('NotLoginStatus'))
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)




class DeleteLabel(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Labels
    template_name = 'labels/delete.html'
    success_url = '/labels/'
    context_object_name = 'labels'
    login_url = 'login'
    success_message = 'Метка успешно удалена'
    error_url = '/statuses/'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('NotLoginStatus'))
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if self.get_object().tasks_set.exists() > 0:
            messages.error(request, _('CannotDeleteLabel'))
            return redirect(reverse('labels'))
        messages.success(self.request, self.success_message)
        return super(DeleteLabel, self).delete(request, *args, **kwargs)
