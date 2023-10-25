import pandas as pd
from dash_funcs.vantage_base import vantageBase

class USeconData(vantageBase):
    def real_gdp(self, period:str="quarterly"):
        url = self.url + f'function=REAL_GDP&interval={period}&{self.apistr}&{self.datatype}'
        df = self.getData(url)
        df.columns = ['date','real_gdp']
        df.set_index('date', inplace = True)
        return df.dropna()
    
    def real_gdp_per_capita(self):
        url = self.url + f'function=REAL_GDP_PER_CAPITA&{self.apistr}&{self.datatype}'
        df = self.getData(url)
        df.columns = ['date', 'real_gdp_per_capita']
        df.set_index('date', inplace = True)
        return df.dropna()

    def cpi(self, interval:str="monthly"):
        url = self.url + f'function=CPI&{self.apistr}&interval={interval}&{self.datatype}'
        df = self.getData(url)
        df.columns = ['date', 'cpi']
        df.set_index('date', inplace = True)
        return df.dropna()

    def inflation(self):
        '''DEPRECATED'''
        url = self.url + f'function=INFLATION&{self.apistr}&{self.datatype}'
        return self.getData(url)

    def retail_sales(self):
        ''' DEPRECATED '''
        url = self.url + f'function=REATIL_SALES&{self.apistr}&{self.datatype}'
        df = self.getData(url)
        df.columns = ['date', 'retail_sales']
        df.set_index('date', inplace = True)
        return df

    def durables(self):
        url = self.url + f'function=DURABLES&{self.apistr}&{self.datatype}'
        df = self.getData(url)
        df.columns = ['date', 'durables']
        df.set_index('date', inplace = True)
        return df.dropna()

    def unemployment(self):
        url = self.url + f'function=UNEMPLOYMENT&{self.apistr}&{self.datatype}'
        df = self.getData(url)
        df.columns = ['date', 'unemployment']
        df.set_index('date', inplace = True)
        return df.dropna()

    def nonfarm_payroll(self):
        '''Deprecated'''
        url = self.url + f'function=NONFARM_PAYROLL&{self.apistr}&{self.datatype}'
        df = self.getData(url)
        df.columns = ['date', 'non_farms']
        df.set_index('date', inplace = True)
        return df.dropna()

    def getAllData(self):
        df = [self.real_gdp(), self.real_gdp_per_capita(), self.cpi(),
        self.durables(), self.unemployment()]
        df = pd.concat(df, axis = 1)
        return df

