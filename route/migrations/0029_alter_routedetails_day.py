# Generated by Django 4.2.1 on 2023-07-30 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0028_alter_routedetails_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routedetails',
            name='day',
            field=models.CharField(choices=[('Sunday', 'Sunday'), ('Tuesday', 'Tuesday'), ('Saturday', 'Saturday'), ('Monday', 'Monday'), ('Friday', 'Friday'), ('Thursday', 'Thursday'), ('Wednesday', 'Wednesday')], max_length=20),
        ),
    ]