# Generated by Django 4.2.1 on 2023-07-30 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0029_alter_routedetails_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routedetails',
            name='day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Thursday', 'Thursday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Sunday', 'Sunday'), ('Saturday', 'Saturday'), ('Friday', 'Friday')], max_length=20),
        ),
    ]
