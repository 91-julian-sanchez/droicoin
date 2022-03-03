from typing import Any

class Cryptocurrency:
    _id= int
    _name= str
    _symbol= str
    _price= int
    _num_market_pairs= int
    _date_added= str
    _max_supply= int
    _circulating_supply= int
    _total_supply= int
    _cmc_rank= int
    _last_updated= str,
    _percent_changes = Any
    def __init__(
        self, id, name, symbol, price,
        num_market_pairs=None, 
        max_supply=None, circulating_supply=None, total_supply=None, 
        cmc_rank=None, last_updated=None, date_added=None,
        percent_changes=None
    ) -> None:
        self._id = id 
        self._name = name
        self._symbol = symbol
        self._price = price
        self._num_market_pairs = num_market_pairs
        self._date_added = date_added
        self._max_supply = max_supply
        self._circulating_supply = circulating_supply
        self._total_supply = total_supply
        self._cmc_rank = cmc_rank
        self._last_updated = last_updated
        self._percent_changes = percent_changes
        pass
    
class CryptocurrencyPercentChange:
    _change_1h = int
    _change_24h = int
    _change_7d = int
    _change_30d = int
    _change_60d = int
    _change_90d = int
    def __init__(self, change_1h=0, change_24h=0, change_7d=0, change_30d=0, change_60d=0, change_90d=0) -> None:
        self._change_1h = change_1h
        self._change_24h = change_24h
        self._change_7d = change_7d
        self._change_30d = change_30d
        self._change_60d = change_60d
        self._change_90d = change_90d
        pass