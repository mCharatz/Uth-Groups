# Generated by Django 3.2 on 2021-10-20 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uth_groups_app', '0039_auto_20211020_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseadmins',
            name='more',
            field=models.BooleanField(default=False),
        ),
    ]