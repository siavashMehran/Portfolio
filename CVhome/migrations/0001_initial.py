# Generated by Django 3.1.5 on 2021-03-25 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='images/')),
                ('title', models.CharField(blank=True, max_length=80)),
                ('grey', models.CharField(blank=True, max_length=80)),
                ('bigImg', models.ImageField(upload_to='images/')),
                ('p1', models.CharField(max_length=400)),
                ('p2', models.CharField(max_length=400)),
                ('slang', models.CharField(max_length=200)),
                ('github', models.URLField()),
                ('insta', models.URLField()),
                ('linkedin', models.URLField()),
                ('name', models.CharField(max_length=20)),
                ('myTitle', models.CharField(max_length=20)),
            ],
        ),
    ]
