# Generated by Django 3.2 on 2021-06-20 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uth_groups_app', '0022_uploadedfile_folder_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='calendar_id',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
