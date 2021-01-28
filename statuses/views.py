from .models import Statuses
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import StatusForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import ugettext as _
from django.core.exceptions import ImproperlyConfigured


class StatusView(LoginRequiredMixin, ListView):
    model = Statuses
    template_name = "statuses/main.html"
    context_object_name = 'statuses'
    form_class = StatusForm
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('NotLoginStatus'))
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class CreateStatus(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Task create view."""

    model = Statuses
    form_class = StatusForm
    template_name = 'statuses/create.html'
    success_url = '/statuses/'
    login_url = 'login'
    success_message = _('SuccessCreatingStatus')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('NotLoginStatus'))
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class UpdateStatus(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Statuses
    success_message = _('SuccessChangingStatus')
    template_name = 'statuses/update.html'
    form_class = StatusForm
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('NotLoginStatus'))
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class DeleteStatus(LoginRequiredMixin, DeleteView):
    model = Statuses
    template_name = 'statuses/delete.html'
    field = ['name']
    success_url = '/statuses/'
    login_url = 'tasks'
    error_url = '/statuses/'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('NotLoginStatus'))
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def get_error_url(self):
        if self.error_url:
            return self.error_url.format(**self.object.__dict__)
        else:
            raise ImproperlyConfigured("No error URL to redirect to.")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        error_url = self.get_error_url()
        try:
            self.object.delete()
            messages.success(request, _('SuccessDeletingStatus'))
            return HttpResponseRedirect(success_url)
        except models.ProtectedError:
            messages.error(request, _('CannotDeleteStatus'))
            return HttpResponseRedirect(error_url)
