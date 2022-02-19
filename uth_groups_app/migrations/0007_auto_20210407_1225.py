# Generated by Django 3.0.7 on 2021-04-07 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uth_groups_app', '0006_auto_20210407_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploader',
            name='available_space',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='uploader',
            name='total_space',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='uploader',
            name='used_space',
            field=models.FloatField(default=0),
        ),
    ]
