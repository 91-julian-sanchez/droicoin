import logging
from coinmarketcap import CoinMarketCap
logging.basicConfig(filename='app.log', encoding='utf-8', level=logging.DEBUG)

if __name__ == '__main__':
    logging.info('Entrypoint init') 
    coinMaketCap = CoinMarketCap()
    active_cryptocurrencies = coinMaketCap.fetch('cryptocurrency/listings/latest')