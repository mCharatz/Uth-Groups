# Generated by Django 3.2 on 2021-08-12 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uth_groups_app', '0034_auto_20210812_1702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='is_academic_autorized',
            new_name='is_academic_authorized',
        ),
    ]
