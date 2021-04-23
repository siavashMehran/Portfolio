# Generated by Django 3.1.5 on 2021-04-23 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CVabout', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bigImg', models.ImageField(upload_to='images/')),
                ('p1', models.TextField(max_length=600)),
                ('p2', models.TextField(max_length=600)),
                ('slang', models.CharField(max_length=300)),
            ],
        ),
    ]