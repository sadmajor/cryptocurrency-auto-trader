import os, sys
import django
from datetime import timedelta
from django.utils.timezone import now
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cryptocurrency-auto-trader.settings")
django.setup()

import requests
from bitcoin.models import Account, History, Action
from bitcoin.scripts.bitcoin_spider import bitcoin_spider
from bitcoin.scripts.usd_spider import usd_spider

def get_user():
    the_user = Account.objects.all().order_by('id')
    if len(the_user) < 1:
        the_user = Account.objects.create(bitcoint_ammount= 0, toman_amount=1000000)
    else:
        the_user = the_user[0]
    return the_user

def growth(histories):
    # new list for growth rates
    growth_rate = []
    # for histories in list
    for history in range(1, len(histories)):
        gnumbers = ((histories[history] - histories[history-1]) * 100.0 / histories[history-1])
        growth_rate.append(gnumbers)
    return (sum(growth_rate)/len(growth_rate))


def trader():
    usd_price = bitcoin_spider().amount
    bitcoin_price = usd_spider().amount
    user = get_user()

    last_hour_date_time = now() - timedelta(hours = 1)

    usd_last_hour_history = History.objects.filter(currency='usd', \
        created_at__gte=last_hour_date_time).order_by('created_at').values_list('amount', flat=True)

    bitcoin_last_hour_history = History.objects.filter(currency='usd', \
        created_at__gte=last_hour_date_time).order_by('created_at').values_list('amount', flat=True)

    bit_growth_avrage = growth(bitcoin_last_hour_history)
    usd_growth_average = growth(usd_last_hour_history)

    if (bit_growth_avrage < 0 and usd_growth_average <0) or \
        (usd_growth_average < 0 and -1 * usd_growth_average > bit_growth_avrage):
        Action.objects.create(action_type='sell', \
            bitcoin_transaction_amount = user.bitcoint_ammount, usd_price = usd_price, bitcoin_price = bitcoin_price)
        
        user.toman_amount = user.toman_amount + user.bitcoint_ammount * bitcoin_price * usd_price
        user.bitcoint_ammount = 0
        user.save()
    else:
        Action.objects.create(action_type='buy', bitcoin_transaction_amount = user.toman_amount / (bitcoin_price * usd_price), usd_price = usd_price, bitcoin_price = bitcoin_price)
        
        user.bitcoint_ammount = user.bitcoint_ammount + user.toman_amount /(bitcoin_price * usd_price)
        user.toman_amount = 0
        user.save()

    

if __name__ == "__main__":
    trader()

