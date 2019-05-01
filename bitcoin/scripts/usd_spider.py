import os, sys
import django
from lxml.html import fromstring
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", \
    "cryptocurrency-auto-trader.settings")
django.setup()

import requests
from bitcoin.models import History

from proxy import get_my_proxy

import logging

# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

USD_DATA_SOURCE_URL = "http://www.tgju.org/dollar-chart"
USD_XPATH = '''//*[@id='main']//table[@class='data-table market-table market-section-right']//tbody//tr[@data-market-row='price_dollar_rl']/td[@class='nf'][1]//text()'''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)',
}

def usd_spider():
    usd_data = requests.get(USD_DATA_SOURCE_URL, \
        # proxies=get_my_proxy(), headers=headers\
            ).text
    tree = fromstring(usd_data)

    usd_price = tree.xpath(USD_XPATH)[0]

    price_int_toman = int(''.join([num for num in usd_price if num in '0123456789']))/10

    return History.objects.create(currency="usd", amount=price_int_toman)

if __name__ == "__main__":
    usd_spider()