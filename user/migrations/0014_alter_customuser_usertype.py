# Generated by Django 4.2.1 on 2023-07-29 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_customuser_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='usertype',
            field=models.CharField(choices=[('planter', 'planter'), ('collector', 'collector')], default='collector', max_length=100),
        ),
    ]
