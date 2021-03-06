# Generated by Django 3.2 on 2021-10-20 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uth_groups_app', '0045_auto_20211020_1437'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='groupadmin',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='groupadmin',
            name='group',
        ),
        migrations.RemoveField(
            model_name='groupadmin',
            name='student',
        ),
        migrations.AddField(
            model_name='course',
            name='admins',
            field=models.ManyToManyField(related_name='CourseAdmins', to='uth_groups_app.Student'),
        ),
        migrations.AddField(
            model_name='group',
            name='admins',
            field=models.ManyToManyField(related_name='GroupAdmins', to='uth_groups_app.Student'),
        ),
        migrations.DeleteModel(
            name='CourseAdmin',
        ),
        migrations.DeleteModel(
            name='GroupAdmin',
        ),
    ]
