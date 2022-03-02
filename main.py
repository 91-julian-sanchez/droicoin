from mimetypes import init
import os
from dotenv import load_dotenv
from coinmarketcap import CoinMaketCap
load_dotenv()
COINMARKETCAP_KEY = os.getenv('COINMARKETCAP_KEY')

if __name__ == '__main__':
    print(f"Api key for Coin market cap: {COINMARKETCAP_KEY}")
    coinMaketCap = CoinMaketCap()
    active_cryptocurrencies = coinMaketCap.test_sandbox()