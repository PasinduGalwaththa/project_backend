# Generated by Django 4.2.1 on 2023-07-21 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estate', '0002_estate_estatenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priceperkg', models.FloatField()),
                ('amount', models.FloatField()),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate.estate')),
            ],
        ),
    ]