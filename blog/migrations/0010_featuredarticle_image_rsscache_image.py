# Generated by Django 5.0.4 on 2024-05-03 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_rssfeed_uid_rssfeed_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredarticle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='rsscache',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]