# Generated by Django 5.1.4 on 2025-01-16 18:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_status_alter_prioridad_nivel_alter_task_status_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clasificacion', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Clasificaciones',
            },
        ),
        migrations.AlterModelOptions(
            name='prioridad',
            options={'verbose_name_plural': 'Prioridad'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Status'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name_plural': 'Task'},
        ),
        migrations.AddField(
            model_name='task',
            name='fecha_creacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='fecha_final',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='tecnicos',
            field=models.ManyToManyField(blank=True, related_name='tecnico_tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='clasificacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.clasificacion'),
        ),
    ]
