# Generated by Django 3.2 on 2021-10-20 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uth_groups_app', '0044_auto_20211020_1359'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='courseadmin',
            unique_together={('student', 'course')},
        ),
        migrations.AlterUniqueTogether(
            name='groupadmin',
            unique_together={('student', 'group')},
        ),
    ]
