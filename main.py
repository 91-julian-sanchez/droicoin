import logging
from coinmarketcap import CoinMarketCap
from cryptocurrency import Cryptocurrency
from cryptocurrency import CryptocurrencyPercentChange
logging.basicConfig(filename='app.log', encoding='utf-8', level=logging.DEBUG)
from prettytable import PrettyTable

def printTable(cryptocurrencies):
   
    prettyTable = PrettyTable()
    prettyTable.field_names = [
        # "Name", "Price", "1h%", "24h%", "7d%", "Market Cap", "Volume(24h)", "Circulating Supply", "Max supply", "Percentage Supply" 
        "#", "Name", "Price", "1h%", "24h%", "7d%",  "Circulating Supply", "Max supply"
    ]
    for crypto in cryptocurrencies:
        prettyTable.add_row([
            crypto._cmc_rank,
            crypto._name+" "+crypto._symbol,
            crypto._price,
            crypto._percent_changes._change_1h,
            crypto._percent_changes._change_24h,
            crypto._percent_changes._change_7d,
            # 0,
            # 0,
            crypto._circulating_supply,
            crypto._max_supply,
        ])
    print(prettyTable)
    
if __name__ == '__main__':
    logging.info('Entrypoint init') 
    coinMaketCap = CoinMarketCap()
    cryptocurrencies = []
    for cryptocurrency in  coinMaketCap.fetch('cryptocurrency/listings/latest'):
        cryptocurrencies.append(Cryptocurrency(
            cryptocurrency.get("id"),
            cryptocurrency.get("name"),
            cryptocurrency.get("symbol"),
            cryptocurrency.get("quote").get("USD").get("price"),
            num_market_pairs = cryptocurrency.get("num_market_pairs"),
            date_added = cryptocurrency.get("date_added"),
            max_supply = cryptocurrency.get("max_supply"),
            circulating_supply = cryptocurrency.get("circulating_supply"),
            total_supply = cryptocurrency.get("total_supply"),
            cmc_rank = cryptocurrency.get("cmc_rank"),
            last_updated = cryptocurrency.get("last_updated"),
            percent_changes = CryptocurrencyPercentChange(
                change_1h= cryptocurrency.get("quote").get("USD").get("percent_change_1h"),
                change_24h= cryptocurrency.get("quote").get("USD").get("percent_change_24h"),
                change_7d= cryptocurrency.get("quote").get("USD").get("percent_change_7d"),
                change_30d= cryptocurrency.get("quote").get("USD").get("percent_change_30d"),
                change_60d= cryptocurrency.get("quote").get("USD").get("percent_change_60d"),
                change_90d= cryptocurrency.get("quote").get("USD").get("percent_change_90d"),
            )
        ))
    printTable(cryptocurrencies)
    