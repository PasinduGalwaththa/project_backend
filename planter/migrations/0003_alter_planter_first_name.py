# Generated by Django 4.2.1 on 2023-06-15 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planter', '0002_alter_planter_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planter',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
    ]
