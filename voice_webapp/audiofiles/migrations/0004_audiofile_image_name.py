# Generated by Django 2.2.17 on 2021-02-21 07:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('audiofiles', '0003_auto_20210221_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiofile',
            name='image_name',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='my_img'),
            preserve_default=False,
        ),
    ]
