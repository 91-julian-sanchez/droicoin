from mimetypes import init
import os
from dotenv import load_dotenv
load_dotenv()
COINMARKETCAP_KEY = os.getenv('COINMARKETCAP_KEY')

from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
class CoinMaketCap:
    _session = None
    _url= 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    _parameters = {
        'start':'1',
        'limit':'5000',
        'convert':'USD'
    }
    _headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
    }
    def __init__(self):
        print("CoinMaketCap init...")
        pass
    
    def _session_create(self):
        print("create coinmarketcap sesion")
        self._session = Session()
        
    def _sesion(self):
        if  self._session is None:
            self._session_create()
        self._session.headers.update(self._headers)
        print("successfully logged in!")

    def test_sandbox(self):
        print("test coinmarketcap sesion")
        try:
          self._sesion()
          response =self._session.get(self._url, params=self._parameters)
          data = json.loads(response.text)
          active_cryptocurrencies = []
          if data.get("data") is not None:
              active_cryptocurrencies = data.get("data")
          print(f"return {len(active_cryptocurrencies)} active cryptocurrencies")
          return active_cryptocurrencies
        except (ConnectionError, Timeout, TooManyRedirects) as e:
          print(e)
        pass

if __name__ == '__main__':
    print(f"Api key for Coin market cap: {COINMARKETCAP_KEY}")
    coinMaketCap = CoinMaketCap()
    active_cryptocurrencies = coinMaketCap.test_sandbox()