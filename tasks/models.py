from django.db import models
from django.urls import reverse
from users.models import CustomUser
from statuses.models import Statuses
from labels.models import Labels


class Tasks(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    status = models.ForeignKey(Statuses, on_delete=models.PROTECT)
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="task_assigned_to")
    creator = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="task_created_by")
    labels = models.ManyToManyField(Labels)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        verbose_name = 'task'
        verbose_name_plural = 'tasks'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tasks')
