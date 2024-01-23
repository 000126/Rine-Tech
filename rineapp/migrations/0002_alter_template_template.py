# Generated by Django 5.0 on 2023-12-08 05:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rineapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='template',
            field=models.FileField(upload_to='template', validators=[django.core.validators.FileExtensionValidator(['xlsx', 'xlsm', 'xltx'])]),
        ),
    ]
