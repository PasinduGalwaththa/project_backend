# Generated by Django 4.2.1 on 2023-07-30 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_alter_customuser_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='usertype',
            field=models.CharField(choices=[('collector', 'collector'), ('planter', 'planter')], default='collector', max_length=100),
        ),
    ]
