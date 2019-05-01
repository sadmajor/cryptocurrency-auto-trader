# coding=utf8
from django.db import models

# Create your models here.

class Account(models.Model):
    bitcoint_ammount = models.FloatField(u'مقدار بیت کوین', editable=False)
    toman_amount = models.IntegerField(u'مقدار تومان', editable=False)

class History(models.Model):
    CURRENCY_TYPE = (
        ('usd', 'usd -> toman'),
        ('bitcoin', 'bitcoin -> usd')
    )
    created_at = models.DateTimeField(u'تاریخ ایجاد', auto_now_add=True)
    currency = models.CharField(u'ارز', max_length=60, choices=CURRENCY_TYPE)
    amount = models.IntegerField(u'مقدار', editable=False)

    def __str__(self):
        return self.currency

class Action(models.Model):
    ACTION_TYPE = (
        ('sell', 'sell bitcoin'),
        ('buy', 'buy bitcoin')
    )
    timestamp = models.DateTimeField(u'تاریخ', auto_now_add=True)
    action_type = models.CharField(u'نوع تراکنش', max_length=60, choices=ACTION_TYPE, editable=False)
    bitcoin_transaction_amount = models.FloatField(u'مقدار بیت کوین معامله شده', editable=False, null=False)
    usd_price = models.IntegerField(u'قیمت دلار به تومان', editable=False)
    bitcoin_price = models.IntegerField(u'قیمت بیت کوین به دلار', editable=False)
