# Generated by Django 5.1.4 on 2024-12-13 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_area'),
        ('usuarios', '0003_alter_usuario_rol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='tecnico',
        ),
        migrations.AddField(
            model_name='task',
            name='tecnicos',
            field=models.ManyToManyField(related_name='tecnico_tasks', to='usuarios.usuario'),
        ),
    ]
