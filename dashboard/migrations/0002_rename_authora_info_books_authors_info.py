# Generated by Django 3.2.5 on 2021-11-29 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='authora_info',
            new_name='authors_info',
        ),
    ]
