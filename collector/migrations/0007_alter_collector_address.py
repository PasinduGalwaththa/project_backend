# Generated by Django 4.2.1 on 2023-07-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0006_collector_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collector',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]
