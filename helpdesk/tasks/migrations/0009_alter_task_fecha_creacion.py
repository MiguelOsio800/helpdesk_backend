# Generated by Django 5.1.4 on 2025-01-16 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_clasificacion_alter_prioridad_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]