# Generated by Django 3.0.7 on 2021-04-07 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uth_groups_app', '0004_uploader'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploader',
            name='base_id',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='uploader',
            name='private',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='uploader',
            name='shorcut_id',
            field=models.CharField(default=0, max_length=200),
        ),
    ]