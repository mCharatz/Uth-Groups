# Generated by Django 3.2 on 2021-08-07 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uth_groups_app', '0025_auto_20210707_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='googleevent',
            name='owner',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='EventOwner', to='uth_groups_app.student'),
        ),
    ]
