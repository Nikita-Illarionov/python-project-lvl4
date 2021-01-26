# Generated by Django 3.1.5 on 2021-01-26 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('labels', '0001_initial'),
        ('tasks', '0002_auto_20210126_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='executor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='task_executor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='label',
            field=models.ManyToManyField(blank=True, to='labels.Labels'),
        ),
    ]
