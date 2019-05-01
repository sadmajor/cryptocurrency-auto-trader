import os, sys
import django
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cryptocurrency-auto-trader.settings")
django.setup()

import requests
from bitcoin.models import History

BITCOIN_DATA_SOURCE_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

def bitcoin_spider():
    bitcoin_data = requests.get(BITCOIN_DATA_SOURCE_URL).json()
    bitcoin_price = bitcoin_data["bpi"]["USD"]["rate_float"]

    return History.objects.create(currency="bitcoin", amount=bitcoin_price)

if __name__ == "__main__":
    bitcoin_spider()

