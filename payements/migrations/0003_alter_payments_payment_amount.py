# Generated by Django 4.2.1 on 2023-07-29 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payements', '0002_rename_amount_payments_payment_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='payment_amount',
            field=models.FloatField(null=True),
        ),
    ]