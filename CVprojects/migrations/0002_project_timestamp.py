# Generated by Django 3.1.5 on 2021-03-28 22:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CVprojects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
