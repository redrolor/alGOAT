# Generated by Django 3.0.7 on 2021-01-18 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buddyrequest', '0006_auto_20210117_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buddyrequest',
            name='profile_picture',
        ),
    ]
