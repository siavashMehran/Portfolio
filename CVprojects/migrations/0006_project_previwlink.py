# Generated by Django 3.1.5 on 2021-05-11 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CVprojects', '0005_auto_20210409_0656'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='PreviwLink',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
