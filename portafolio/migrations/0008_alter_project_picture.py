# Generated by Django 4.2 on 2023-05-11 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0007_alter_project_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='picture',
            field=models.ImageField(upload_to='projects', verbose_name='Imagen'),
        ),
    ]
