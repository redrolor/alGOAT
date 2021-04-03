# Generated by Django 3.0.7 on 2021-01-17 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buddyrequest', '0004_buddyrequest_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='buddyrequest',
            name='bio',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='buddyrequest',
            name='intensity',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='buddyrequest',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='buddyrequest',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='', verbose_name='upload_to="images/"'),
        ),
    ]
