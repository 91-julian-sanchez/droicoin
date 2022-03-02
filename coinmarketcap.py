from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
PARAMETERS = {
    'start':'1',
    'limit':'5000',
    'convert':'USD'
}
class CoinMaketCap:
    _session = None
    _url= str
    _headers = None
    def __init__(self,*args,**kwargs):
        print("CoinMaketCap init...")
        self._url= kwargs.get("url")
        self._headers = kwargs.get("headers")
        pass
    
    def _session_create(self):
        print("create coinmarketcap sesion")
        self._session = Session()
        
    def _sesion(self):
        if  self._session is None:
            self._session_create()
        self._session.headers.update(self._headers)
        print("successfully logged in!")

    def test_sandbox(self, parameters=PARAMETERS):
        print("test coinmarketcap sesion")
        try:
          self._sesion()
          response = self._session.get(f"{self._url}/listings/latest", params=parameters)
          data = json.loads(response.text)
          active_cryptocurrencies = []
          if data.get("data") is not None:
              active_cryptocurrencies = data.get("data")
          print(f"return {len(active_cryptocurrencies)} active cryptocurrencies")
          return active_cryptocurrencies
        except (ConnectionError, Timeout, TooManyRedirects) as e:
          print(e)
        pass