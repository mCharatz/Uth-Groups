# Generated by Django 3.0.7 on 2021-04-08 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uth_groups_app', '0008_auto_20210408_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploader',
            name='available_space',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='uploader',
            name='total_space',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='uploader',
            name='used_space',
            field=models.FloatField(default=0),
        ),
    ]
