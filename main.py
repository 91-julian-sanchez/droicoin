import os
from dotenv import load_dotenv
load_dotenv()
COINMARKETCAP_KEY = os.getenv('COINMARKETCAP_KEY')

if __name__ == '__main__':
    print(f"Api kay for Coin market cap: {COINMARKETCAP_KEY}")