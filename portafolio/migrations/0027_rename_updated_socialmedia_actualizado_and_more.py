# Generated by Django 4.2 on 2023-05-13 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0026_remove_socialmedia_facebook_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialmedia',
            old_name='updated',
            new_name='actualizado',
        ),
        migrations.RenameField(
            model_name='socialmedia',
            old_name='created',
            new_name='creado',
        ),
    ]
