# Generated by Django 3.2.5 on 2021-11-29 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_logger'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logger',
            name='date',
        ),
    ]
