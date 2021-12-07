# Generated by Django 3.0.5 on 2021-08-15 12:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=25)),
                ('last_name', models.CharField(default='', max_length=25)),
                ('email_id', models.CharField(default='', max_length=320, unique=True)),
                ('contact_number', models.CharField(default='', max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('permanent_address', models.CharField(default='', max_length=100)),
                ('education_qualification', models.CharField(default='', max_length=25)),
                ('active_status', models.CharField(default='', max_length=10)),
            ],
        ),
    ]
