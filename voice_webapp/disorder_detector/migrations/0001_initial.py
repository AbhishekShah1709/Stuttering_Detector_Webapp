# Generated by Django 3.1.7 on 2021-02-23 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.TextField()),
                ('file_details', models.FileField(upload_to='')),
            ],
        ),
    ]
