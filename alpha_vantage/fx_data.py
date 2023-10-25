import pandas as pd
from dash_funcs.vantage_base import vantageBase

class fxData(vantageBase):
    def FX_daily(self, from_currency:str, to_currency:str, outputsize="compact"):
        '''return OHLC data for pair'''
        url = self.url + f'function=FX_DAILY&from_symbol={from_currency}&to_symbol={to_currency}&{self.apistr}&{self.datatype}'
        df = self.getData(url)
        df.columns = ['date',f'{from_currency}/{to_currency}_open',
                    f'{from_currency}/{to_currency}_high',
                    f'{from_currency}/{to_currency}_low',
                    f'{from_currency}/{to_currency}_close']
        return df

    def FX_intraday(self, from_currency:str, to_currency:str, period:str = "5min", outputsize="compact"):
        url = self.url + f'function=FX_DAILY&from_symbol={from_currency}&to_symbol={to_currency}&interval={period}&{self.apistr}&{self.datatype}'
        df = self.getData(url)
        return df

    def realTimeFX(self,from_currency:str, to_currency:str):
        url = self.url + f'function=CURRENCY_EXCHANGE_RATE&from_symbol={from_currency}&to_symbol={to_currency}&{self.apistr}'
        df = self.getData(url)
        return df