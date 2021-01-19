from .models import Statuses
from django.views.generic import UpdateView, DeleteView, ListView
from .forms import StatusForm
from django.shortcuts import render, redirect



class StatusView(ListView):
    model = Statuses
    template_name = "statuses/statuses.html"
    context_object_name = 'statuses'



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



class UpdateStatus(UpdateView):
    model = Statuses
    template_name = 'statuses/update.html'
    field = ['name']
    form_class = StatusForm



class DeleteStatus(DeleteView):
    model = Statuses
    template_name = 'statuses/delete.html'
    field = ['name']
    success_url = '/statuses/'
