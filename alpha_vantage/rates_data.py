from dash_funcs.vantage_base import vantageBase
import pandas as pd 
import requests

class USratesData(vantageBase):
    def US_treasury_yield(self, interval:str="quarterly", maturity:str="3month"):
        '''interval options: daily/weekly/monthly/quarterly
       maturity options: 3month/2year/5year/7year/10year/30year
        '''
        url = self.url + f'function=TREASURY_YIELD&{self.apistr}&interval={interval}&maturity={maturity}&{self.datatype}'
        df = self.getData(url)
        df.columns = ['date', f'{maturity}']
        df.set_index('date', inplace = True)
        return df

    def US_federal_funds_rate(self, interval:str="quarterly"):
        '''interval options: daily/weekly/monthly/quarterly
        '''
        url = self.url + f'function=FEDERAL_FUNDS_RATE&{self.apistr}&interval={interval}&{self.datatype}'
        df = self.getData(url)
        df.set_index('date', inplace = True)
        df.columns = [f'{maturity}']
        return df

    def get_US_treasury_yield_curve(self, period:str):
        daily = [self.US_treasury_yield(f'{period}', '3month'), 
                self.US_treasury_yield(f'{period}', '2year'),
                self.US_treasury_yield(f'{period}', '5year'), 
                self.US_treasury_yield(f'{period}', '10year'), 
                self.US_treasury_yield(f'{period}', '30year')]  
        
        daily['50MA_10yr'] = daily['10year'].rolling_mean(window = 50).mean()
        daily['50MA_3m'] = daily['10year'].rolling_mean(window = 50).mean()
        daily['Rec_Ind'] = daily['50MA_10yr'] - daily['50MA_3m']
        return pd.concat(daily, axis=1)

