# Generated by Django 3.1.5 on 2023-03-29 12:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_information', '0004_auto_20230329_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='end_time',
            field=models.TimeField(default=datetime.time(20, 0)),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='start_time',
            field=models.TimeField(default=datetime.time(20, 0)),
        ),
    ]