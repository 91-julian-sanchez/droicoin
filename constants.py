import os
from dotenv import load_dotenv
load_dotenv()
SANDBOX = True
COINMARKETCAP_URL = os.getenv('COINMARKETCAP_SANDBOX_URL') if SANDBOX is True else os.getenv('COINMARKETCAP_URL')
COINMARKETCAP_APIKEY = os.getenv('COINMARKETCAP_SANDBOX_APIKEY') if SANDBOX is True else os.getenv('COINMARKETCAP_APIKEY')