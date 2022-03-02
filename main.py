import os
from dotenv import load_dotenv
from coinmarketcap import CoinMaketCap
load_dotenv()
COINMARKETCAP_KEY = os.getenv('COINMARKETCAP_KEY')

if __name__ == '__main__':
    print(f"Api key for Coin market cap: {COINMARKETCAP_KEY}")
    coinMaketCap = CoinMaketCap(
        headers={
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
        },
        url= os.getenv('COINMARKETCAP_URL')
    )
    active_cryptocurrencies = coinMaketCap.test_sandbox()