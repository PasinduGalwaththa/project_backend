# Generated by Django 4.2.1 on 2023-07-18 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='collector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('nic', models.CharField(max_length=4)),
                ('adress', models.CharField(max_length=20)),
                ('telephone', models.CharField(max_length=10)),
            ],
        ),
    ]
