# Generated by Django 4.2.1 on 2023-07-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estatename', models.CharField(max_length=20, null=True)),
                ('teatype', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
