# Generated by Django 3.1.5 on 2023-04-06 12:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_center', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='contact_no',
            field=models.CharField(default='0000000000', max_length=10, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]