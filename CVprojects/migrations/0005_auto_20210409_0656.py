# Generated by Django 3.1.5 on 2021-04-09 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CVprojects', '0004_auto_20210403_0536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='imageSub1',
        ),
        migrations.RemoveField(
            model_name='project',
            name='imageSub2',
        ),
        migrations.RemoveField(
            model_name='project',
            name='imageSub3',
        ),
    ]
