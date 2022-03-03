import json
import logging
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

class HttpClient:
    _url= str
    _headers = None
    _session = None
    def __init__(self, *args, **kwargs) -> None:
        self._headers = kwargs.get('headers') if kwargs.get('headers') else None
        self._params = kwargs.get('params') if kwargs.get('params') else None
        pass
    
    def _session_create(self):
        logging.info("initializing session")
        self._session = Session()
        
    def _sesion(self):
        if  self._session is None:
            self._session_create()
        self._session.headers.update(self._headers)
        logging.info("successfully session created!")
        
    def get(self, url, params=None, headers=None):
        logging.info(f"Fetch (GET) {url}")
        if params is None:
            params = self._params
        if headers is None:
            headers = self._headers
        try:
            self._sesion()
            response = self._session.get(url, params=params)
            logging.info(f"Fetch (GET) {url}")
            return json.loads(response.text)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
          logging.error(f"Fetch (GET) {url}")
          print(e)