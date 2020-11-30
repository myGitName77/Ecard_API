# Generated by Django 3.1.2 on 2020-11-26 09:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('employee_number', models.IntegerField()),
                ('email', models.EmailField(default=False, max_length=100)),
                ('UID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('access_level', models.IntegerField(default=False)),
            ],
        ),
    ]
