# Generated by Django 3.2 on 2021-08-10 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uth_groups_app', '0026_googleevent_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='uth_groups_app.course')),
                ('group', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='uth_groups_app.group')),
                ('participants', models.ManyToManyField(to='uth_groups_app.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, default='', max_length=2000, null=True)),
                ('chat', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='uth_groups_app.chat')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uth_groups_app.student')),
            ],
        ),
    ]
