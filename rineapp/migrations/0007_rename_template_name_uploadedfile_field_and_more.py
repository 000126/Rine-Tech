# Generated by Django 5.0 on 2024-02-05 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rineapp', '0006_alter_template_a_r_no_alter_template_batch_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadedfile',
            old_name='template_name',
            new_name='field',
        ),
        migrations.RemoveField(
            model_name='uploadedfile',
            name='template_number',
        ),
        migrations.RemoveField(
            model_name='uploadedfile',
            name='template_type',
        ),
        migrations.RemoveField(
            model_name='uploadedfile',
            name='user',
        ),
    ]
