# Generated by Django 3.1.5 on 2021-03-26 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=18)),
                ('messege', models.TextField(max_length=500)),
            ],
        ),
    ]
