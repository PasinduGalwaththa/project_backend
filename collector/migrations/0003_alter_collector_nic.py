# Generated by Django 4.2.1 on 2023-07-26 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0002_collector_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collector',
            name='nic',
            field=models.CharField(max_length=12),
        ),
    ]
