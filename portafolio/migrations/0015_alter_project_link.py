# Generated by Django 4.2 on 2023-05-12 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0014_alter_project_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Direccion web'),
        ),
    ]