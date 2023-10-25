import pandas as pd
from dash_funcs.alpha_vantage.rates_data import USratesData
from dash_funcs.alpha_vantage.economic_data import USeconData
from dash_funcs.alpha_vantage.commodities_data import commoditiesData
from dash_funcs.alpha_vantage.equity_data import EquityData
class DS():
    def __init__(self):
        "TODO: This needs to be multiprocessed"
        #self.US_rates = self.getUSrates()
        self.US_econ = self.getUSEconomicData()
        #self.oil_and_gas = commoditiesData().gas_and_oil()
        self.ec = self.earningsCalendars()

    def earningsCalendars(self):
        e = EquityData()
        dataframes = {
            "3month": e.earningsCalendarData("3month").dropna(0),
            "6month": e.earningsCalendarData("6month").dropna(0),
            "12month": e.earningsCalendarData("12month").dropna(0), 
        }
        return dataframes

    def getUSrates(self) -> pd.DataFrame():
        daily = None
        while daily is None:
            try:
                r = USratesData()
                daily = r.get_US_treasury_yield_curve('daily')
                daily.columns = ['yld_3mo', 'yld_2yr', 'yld_5yr', 'yld_10yr', 'yld_30yr']
            except Exception as e: 
                print(e)
                print("Error in US rates")
        return daily

    def getUSEconomicData(self) -> pd.DataFrame():
        result = None
        while result is None:
            try:
                result = USeconData().getAllData()
            except Exception as e:
                print(e)
                print("Error in US Econ")
        return result

    def getUSrates2(self) -> pd.DataFrame():
        pass

    def getUSEconomicData2(self) -> pd.DataFrame():
        "multi-threaded for each data call"
        pass