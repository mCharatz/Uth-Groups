# Generated by Django 3.2 on 2021-05-17 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uth_groups_app', '0020_course_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=200, null=True)),
                ('file', models.FileField(upload_to='')),
                ('course', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='uth_groups_app.course')),
                ('group', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='uth_groups_app.group')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uth_groups_app.student')),
            ],
        ),
    ]
