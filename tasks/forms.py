from .models import Tasks
from django.forms import ModelForm, TextInput


class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['name', 'description', 'status', 'executor', 'label']
