from coinmarketcap import CoinMarketCap

if __name__ == '__main__':
    coinMaketCap = CoinMarketCap()
    active_cryptocurrencies = coinMaketCap.fetch('cryptocurrency/listings/latest')