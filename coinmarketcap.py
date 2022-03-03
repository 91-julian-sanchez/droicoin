import logging
import json
from http_client import HttpClient
from constants import COINMARKETCAP_URL
from constants import COINMARKETCAP_APIKEY
from constants import PARAMETERS

def request_validator(func):
    _available_endpoint_categories = [
        "cryptocurrency", #Endpoints that return data around cryptocurrencies such as ordered cryptocurrency lists or price and volume data.
        "exchange", #Endpoints that return data around cryptocurrency exchanges such as ordered exchange lists and market pair data.
        "global-metrics", #Endpoints that return aggregate market data such as global market cap and BTC dominance.
        "tools", #Useful utilities such as cryptocurrency and fiat price conversions.
        "blockchain", #Endpoints that return block explorer related data for blockchains.
        "fiat", #Endpoints that return data around fiats currencies including mapping to CMC IDs.
        "partners", #Endpoints for convenient access to 3rd party crypto data.
        "key", #API key administration endpoints to review and manage your usage.
    ]
    _available_endpoint_paths = [
        'latest', #Latest market ticker quotes and averages for cryptocurrencies and exchanges.
        'historical', #Intervals of historic market data like OHLCV data or data for use in charting libraries.
        'info', #Cryptocurrency and exchange metadata like block explorer URLs and logos.
        'map' #Utility endpoints to get a map of resources to CoinMarketCap IDs.
    ]
    _available_endpoints_kind_get = [
        "listings", #Flexible paginated */listings/* endpoints allow you to sort and filter lists of data like cryptocurrencies
        "quotes", #this allows you to get latest market quotes for a specific set of cryptocurrencies in one call
        "market-pairs" 
    ]
    def wrapper(*args):
        endpoint_category, kind_get, endpoint_path  = None, None, None
        url_string_params = tuple(args[1].split("/"))
        if len(url_string_params) == 3:
            endpoint_category, kind_get, endpoint_path  = url_string_params[0], url_string_params[1], url_string_params[2]
            if kind_get not in _available_endpoints_kind_get:
                raise TypeError("ERROR: Invalid endpoint(0)!!")
        elif len(url_string_params) == 2:
            endpoint_category, endpoint_path  = url_string_params[0], url_string_params[1]
        else:
            raise TypeError("ERROR: Invalid endpoint(1)!!")
    
        # print("endpoint_category: ", endpoint_category)
        # print("kind_get: ", kind_get)
        # print("endpoint_path: ", endpoint_path)
        
        if endpoint_category not in _available_endpoint_categories or endpoint_path not in _available_endpoint_paths:
            raise TypeError("ERROR: Invalid endpoint!!")
        else:
            return func(args[0], args[1])
    return wrapper            

def output(data):
    jsonString = json.dumps(data)
    jsonFile = open("data.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
    
class CoinMarketCap:
    _session = None
    _headers = None
    def __init__(self):
        logging.info('CoinMarketCap::class init')
        logging.info(f"Apikey for Coin market cap: {COINMARKETCAP_APIKEY}")
        self._headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': COINMARKETCAP_APIKEY,
        }
        pass
    @request_validator
    def fetch(self, path, parameters=PARAMETERS) -> object:
        logging.info(f'CoinMarketCap::fetch fetch {COINMARKETCAP_URL}/{path}')
        httpClient = HttpClient(headers=self._headers)
        response = httpClient.get(f"{COINMARKETCAP_URL}/{path}", params=parameters)
        # response = {
        #     "data":[],
        #     "status": {
        #         "timestamp": "2018-06-06T07:52:27.273Z",
        #         "error_code": 400,
        #         "error_message": "Invalid value for \"id\"",
        #         "elapsed": 0,
        #         "credit_count": 0
        #     }
        # } 
        print(f"return {len(response.get('data'))} active cryptocurrencies")
        output(response.get("data"))
        return response.get("data")
