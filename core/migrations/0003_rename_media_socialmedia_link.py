# Generated by Django 4.2 on 2023-05-13 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_creado_socialmedia_created_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialmedia',
            old_name='media',
            new_name='link',
        ),
    ]
