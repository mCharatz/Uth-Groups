# Generated by Django 3.2 on 2021-08-16 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uth_groups_app', '0037_student_academic_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='academic_email',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='academic_name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='academic_status',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='authorization_code',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
