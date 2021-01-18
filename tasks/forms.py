from .models import Statuses, Tags
from django.forms import ModelForm, TextInput


class StatusesForm(ModelForm):
    class Meta:
        model = Statuses
        fields = ['name']

        widgets = {'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статуса'})}



class TagsForm(ModelForm):
    class Meta:
        model = Tags
        fields = ['name']

        widgets = {'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название тега'})}

    
