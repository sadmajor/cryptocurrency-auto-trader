# Generated by Django 2.0.13 on 2019-04-28 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitcoin', '0003_auto_20190426_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bitcoint_ammount', models.IntegerField(editable=False, verbose_name='مقدار بیت کوین')),
                ('toman_amount', models.IntegerField(editable=False, verbose_name='مقدار تومان')),
            ],
        ),
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')),
                ('action_type', models.CharField(choices=[('sell', 'sell bitcoin'), ('buy', 'buy bitcoin')], max_length=60, verbose_name='نوع تراکنش')),
                ('amount', models.IntegerField(editable=False, verbose_name='مقدار بیت کوین معامله شده')),
                ('dollar_price', models.IntegerField(editable=False, verbose_name='قیمت دلار به تومان')),
                ('bitcoin_price', models.IntegerField(editable=False, verbose_name='قیمت بیت کوین به دلار')),
            ],
        ),
    ]
