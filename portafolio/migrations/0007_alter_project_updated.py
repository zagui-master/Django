# Generated by Django 4.2 on 2023-05-11 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0006_alter_project_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha actualizacion'),
        ),
    ]
