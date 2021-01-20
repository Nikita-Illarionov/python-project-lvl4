import django_filters
from .models import Tasks

class TasksFilter(django_filters.FilterSet):

    class Meta:
        model = Tasks
        fields = ['status', 'assigned_to', 'labels', 'creator']
