# Generated by Django 4.2.1 on 2023-07-30 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payements', '0012_alter_payments_teatype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='calculated_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
