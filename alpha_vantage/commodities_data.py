import pandas as pd

from dash_funcs.vantage_base import vantageBase

class commoditiesData(vantageBase):
    def WTI(self, period:str = "daily"):
        url = self.url + f'function=WTI&interval={period}&{self.apistr}&{self.datatype}'
        df = self.getData(url)
        df.columns = ['date','wti']
        df.set_index('date', inplace = True)
        return df
    
    def Brent(self, period:str = "daily"):
        url = self.url + f'function=BRENT&interval={period}&{self.apistr}&{self.datatype}'
        df = self.getData(url)
        df.columns = ['date','brent']
        df.set_index('date', inplace = True)
        return df

    def NatGas(self, period:str = "daily"):
        url = self.url + f'function=NATURAL_GAS&interval={period}&{self.apistr}&{self.datatype}'
        df = self.getData(url)
        df.columns = ['date','brent']
        df.set_index('date', inplace = True)
        return df

    def gas_and_oil(self):
        return pd.concat([self.WTI(), self.Brent(), self.NatGas()], axis = 1)