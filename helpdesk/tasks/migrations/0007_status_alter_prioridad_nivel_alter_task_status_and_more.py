# Generated by Django 5.1.4 on 2025-01-09 20:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_estado_alter_task_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='prioridad',
            name='nivel',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.status'),
        ),
        migrations.DeleteModel(
            name='Estado',
        ),
    ]