# Generated by Django 2.0.13 on 2019-04-30 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitcoin', '0006_auto_20190428_1800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='action',
            old_name='dollar_price',
            new_name='usd_price',
        ),
    ]
