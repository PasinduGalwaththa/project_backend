# Generated by Django 4.2.1 on 2023-07-30 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0008_alter_routedetails_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routedetails',
            name='day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Sunday', 'Sunday'), ('Saturday', 'Saturday'), ('Tuesday', 'Tuesday'), ('Friday', 'Friday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday')], max_length=20),
        ),
    ]
