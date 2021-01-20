from .models import Tasks
from django.forms import ModelForm, TextInput


class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['name', 'status', 'assigned_to']
