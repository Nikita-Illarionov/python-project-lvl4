from .models import Labels
from django.forms import ModelForm, TextInput


class LabelForm(ModelForm):
    class Meta:
        model = Labels
        fields = ['name']

        widgets = {'name': TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Имя'})}
