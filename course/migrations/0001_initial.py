# Generated by Django 4.2 on 2024-10-06 17:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('date', models.DateField(verbose_name=datetime.date.today)),
                ('hours', models.CharField(max_length=20)),
            ],
        ),
    ]
