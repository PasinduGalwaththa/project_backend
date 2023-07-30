# Generated by Django 4.2.1 on 2023-07-30 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planter', '0002_initial'),
        ('payements', '0008_remove_payments_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='planter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='planter.planter'),
            preserve_default=False,
        ),
    ]
