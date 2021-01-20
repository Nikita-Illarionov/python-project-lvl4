from .models import Statuses
from django.views.generic import UpdateView, DeleteView, ListView
from .forms import StatusForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin



class StatusView(LoginRequiredMixin, ListView):
    model = Statuses
    template_name = "statuses/statuses.html"
    context_object_name = 'statuses'
    form_class = StatusForm
    login_url = 'login'



def create_status(request):
    error = ''
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('statuses')
        else:
            error = 'Форма заполнена неверно'

    form = StatusForm()
    data = {'form': form, 'error': error}
    return render(request, 'statuses/create.html', data)



class UpdateStatus(LoginRequiredMixin, UpdateView):
    model = Statuses
    template_name = 'statuses/update.html'
    form_class = StatusForm
    login_url = 'login'



class DeleteStatus(LoginRequiredMixin, DeleteView):
    model = Statuses
    template_name = 'statuses/delete.html'
    field = ['name']
    success_url = '/statuses/'
    login_url = 'login'
