# Generated by Django 4.2 on 2023-05-11 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0009_alter_project_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='picture',
            field=models.ImageField(upload_to='projects', verbose_name='Imagen'),
        ),
    ]
