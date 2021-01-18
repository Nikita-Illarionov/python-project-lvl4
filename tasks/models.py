from django.db import models
from django.urls import reverse


class Tasks(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    creator = models.CharField(max_length=100)
    assigned_to = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    tags = models.CharField(max_length=50)

    class Meta(object):
        verbose_name = 'task'
        verbose_name_plural = 'tasks'

    def __str__(self):
        return self.name


class Statuses(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        verbose_name = 'status'
        verbose_name_plural = 'statuses'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('statuses')



class Tags(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tags')
