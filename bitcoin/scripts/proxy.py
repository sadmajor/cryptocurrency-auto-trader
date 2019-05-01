# from stem import Signal
# from stem.control import Controller
# import requests
# import time

def get_my_proxy():
    """ Static method to get proxy
    """
    proxy = 'socks5://127.0.0.1:9050'
    http_proxy = proxy
    https_proxy = proxy
    ftp_proxy = proxy

    proxyDict = {
        "http": http_proxy,
        "https": https_proxy,
        "ftp": ftp_proxy
    }
    return proxyDict

# signal TOR for a new connection 
# def renew_connection(self):
#     with Controller.from_port(port = 9051) as controller:
#         controller.authenticate(password = 'opentor')
#         controller.signal(Signal.NEWNYM)
#     NEXT_IP = None
#     while True:
#         NEXT_IP = requests.get("http://httpbin.org/ip", proxies={'http':  'socks5://127.0.0.1:9050',
#                     'https': 'socks5://127.0.0.1:9050'}).json()["origin"]
#         if self.CURRENT_IP != NEXT_IP:
#             CURRENT_IP = NEXT_IP
#             break
#         time.sleep(2)
#     print("new ip set to: %s"%CURRENT_IP)