# Generated by Django 4.2.1 on 2023-07-30 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0013_alter_routedetails_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routedetails',
            name='day',
            field=models.CharField(choices=[('Sunday', 'Sunday'), ('Saturday', 'Saturday'), ('Monday', 'Monday'), ('Wednesday', 'Wednesday'), ('Friday', 'Friday'), ('Thursday', 'Thursday'), ('Tuesday', 'Tuesday')], max_length=20),
        ),
    ]
