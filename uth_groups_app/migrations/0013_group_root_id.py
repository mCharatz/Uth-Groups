# Generated by Django 3.0.7 on 2021-04-11 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uth_groups_app', '0012_auto_20210408_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='root_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
