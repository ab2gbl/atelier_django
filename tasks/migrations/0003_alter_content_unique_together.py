# Generated by Django 4.2.3 on 2023-08-15 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_content_content_type'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='content',
            unique_together={('task', 'index')},
        ),
    ]
