# Generated by Django 5.0.4 on 2024-05-01 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rssfeed_featuredarticle_order_rsscache'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredarticle',
            name='summary',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='rsscache',
            name='summary',
            field=models.TextField(),
        ),
    ]