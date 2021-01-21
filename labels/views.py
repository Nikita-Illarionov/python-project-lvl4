from django.shortcuts import render, redirect
from .models import Labels
from .forms import LabelForm
from django.views.generic import UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class LabelView(LoginRequiredMixin, ListView):
    model = Labels
    template_name = "labels/labels.html"
    context_object_name = 'labels'
    login_url = 'login'



def create_label(request):
    error = ''
    if request.method == 'POST':
        form = LabelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Метка успешно создана')
            return redirect('labels')
        else:
            error = 'Форма заполнена неверно'


    form = LabelForm()
    data = {'form': form, 'error': error}
    return render(request, 'labels/create.html', data)



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
