# Generated by Django 3.2.5 on 2021-11-29 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_logger_crud_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrudLogger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crud_log', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='logger',
            name='crud_log',
        ),
    ]
