# Generated by Django 4.2.3 on 2023-08-21 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_path_instructor_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='path_instructor',
            old_name='user',
            new_name='instructor',
        ),
    ]
