class Utility(vantageBase):
    pass

    def market_oc(self):
        pass
    
    def ticker_search(self, string:str):
        url = self.url + f'function=SYMBOL_SEARCH&keywords={string}'
        return self.getData(url)