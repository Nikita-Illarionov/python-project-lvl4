from django.shortcuts import render, redirect
from .models import Labels
from .forms import LabelForm
from django.views.generic import UpdateView, DeleteView, ListView


class LabelView(ListView):
    model = Labels
    template_name = "labels/labels.html"
    context_object_name = 'labels'



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



class UpdateLabel(UpdateView):
    model = Labels
    template_name = 'labels/update.html'
    field = ['name']

    form_class = LabelForm




class DeleteLabel(DeleteView):
    model = Labels
    template_name = 'labels/delete.html'
    field = ['name']
    success_url = '/labels/'
