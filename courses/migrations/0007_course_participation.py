# Generated by Django 4.2.3 on 2023-08-22 11:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('courses', '0006_alter_path_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Participation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.developer')),
            ],
        ),
    ]
