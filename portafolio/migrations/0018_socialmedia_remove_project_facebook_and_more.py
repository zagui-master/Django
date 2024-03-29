# Generated by Django 4.2 on 2023-05-13 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0017_project_facebook_project_instragam_project_twitter'),
    ]

    operations = [
        migrations.CreateModel(
            name='socialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Link facebook')),
                ('instragam', models.URLField(blank=True, null=True, verbose_name='Link instagram')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Link twitter')),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='project',
            name='instragam',
        ),
        migrations.RemoveField(
            model_name='project',
            name='twitter',
        ),
    ]
