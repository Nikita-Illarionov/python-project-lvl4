from django.db import models
from django.urls import reverse


class Labels(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        verbose_name = 'label'
        verbose_name_plural = 'labels'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('labels')
