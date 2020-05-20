# Generated by Django 3.0.6 on 2020-05-20 02:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('name', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('icon', models.ImageField(help_text='Upload an image that will appearas an icon for this task on the home page', upload_to='taskicons/')),
                ('trialinfo', models.FileField(upload_to='json/')),
                ('tasktype', models.SmallIntegerField(choices=[(1, 'nAFC'), (2, 'Open-Set')], null=True)),
                ('experimenter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trialnum', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('answer', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Task')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]