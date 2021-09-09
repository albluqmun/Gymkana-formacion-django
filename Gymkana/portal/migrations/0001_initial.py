# Generated by Django 3.2.7 on 2021-09-08 14:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('publish_date', models.DateTimeField(default=datetime.datetime(2021, 9, 8, 14, 38, 44, 458372, tzinfo=utc))),
                ('image', models.ImageField(default='static/portal/images/default.jpg', upload_to='static/portal/images/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
