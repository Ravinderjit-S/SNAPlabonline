# Generated by Django 3.0.6 on 2020-06-01 00:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20200531_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_url',
            field=models.CharField(default='dP90dwx9U92W9d21QEdgH0EsBNs2Ei9KijTUNZoGo88', max_length=32, unique=True),
        ),
    ]
