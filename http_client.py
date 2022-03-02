from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

class HttpClient:
    _url= str
    _headers = None
    _session = None
    def __init__(self, *args, **kwargs) -> None:
        self._headers = kwargs.get('headers') if kwargs.get('headers') else None
        self._params = kwargs.get('params') if kwargs.get('params') else None
        pass
    
    def _session_create(self):
        print("create coinmarketcap sesion")
        self._session = Session()
        
    def _sesion(self):
        if  self._session is None:
            self._session_create()
        self._session.headers.update(self._headers)
        print("successfully logged in!")
        
    def get(self, url, params=None, headers=None):
        print(f"Fetching (GET) {url}")
        if params is None:
            params = self._params
        if headers is None:
            headers = self._headers
        try:
            self._sesion()
            response = self._session.get(url, params=params)
            return json.loads(response.text)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
          print(e)