# Generated by Django 3.0.7 on 2021-04-08 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uth_groups_app', '0011_auto_20210408_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='files_folder_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='folder_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
