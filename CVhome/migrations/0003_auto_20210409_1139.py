# Generated by Django 3.1.5 on 2021-04-09 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CVhome', '0002_auto_20210326_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='p1',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='home',
            name='p2',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='home',
            name='slang',
            field=models.CharField(max_length=300),
        ),
    ]
