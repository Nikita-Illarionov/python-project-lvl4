from .models import Statuses
from django.forms import ModelForm, TextInput


class StatusForm(ModelForm):
    class Meta:
        model = Statuses
        fields = ['name']

        widgets = {'name': TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Имя'})}
