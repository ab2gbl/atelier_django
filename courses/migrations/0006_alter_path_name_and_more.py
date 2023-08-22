# Generated by Django 4.2.3 on 2023-08-21 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('courses', '0005_rename_user_path_instructor_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='path',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='path_instructor',
            unique_together={('path', 'instructor')},
        ),
    ]