from django.shortcuts import render, redirect
from .models import Labels
from .forms import LabelForm
from django.views.generic import UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


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
            return redirect('labels')
        else:
            error = 'Форма заполнена неверно'


    form = LabelForm()
    data = {'form': form, 'error': error}
    return render(request, 'labels/create.html', data)



class UpdateLabel(LoginRequiredMixin, UpdateView):
    model = Labels
    template_name = 'labels/update.html'
    form_class = LabelForm
    login_url = 'login'




class DeleteLabel(LoginRequiredMixin, DeleteView):
    model = Labels
    template_name = 'labels/delete.html'
    success_url = '/labels/'
    context_object_name = 'labels'
    login_url = 'login'
