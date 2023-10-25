from alpha_vantage.vantage_base import vantageBase
import pandas as pd

class EquityData(vantageBase):

    def sheetdata(self, fs, symbol):
        "fs : financial statement | INCOME_STATEMENT/BALANCE_SHEET/CASH_FLOW/EARNINGS"
        url = self.url + f'function={fs}&symbol={symbol}&{self.apistr}'
        df = self.getJson(url)
        df = pd.DataFrame.from_records(df["annualReports"]).T
        df.columns  = df.iloc[0]
        df = df.iloc[2:]
        df[df.columns] = df[df.columns].apply(pd.to_numeric, errors='coerce', axis=1)
        return df

    def earnings(self, symbol):
        url = self.url + f'function=EARNINGS&symbol={symbol}&{self.apistr}'
        df = self.getJson(url)
        return df

    def earningsCalendarData(self, horizon = "3MONTHS"):
        url = self.url + f'function=EARNINGS_CALENDAR&horizon={horizon}&{self.apistr}'
        df = self.getData(url)
        return df

    def ipoCalendarData(self):
        url = self.url + f'function=IPO_CALENDAR&{self.apistr}'
        df = self.getData(url)
        return df
    
    def allsheets(self, symbol):
        inc = self.sheetdata("INCOME_STATEMENT", symbol)
        bs = self.sheetdata("BALANCE_SHEET", symbol)
        cf = self.sheetdata("CASH_FLOW", symbol)
        return [inc, bs, cf]
    
    def ratiosCalc(self, income, balance, cashflow):
        ratios = pd.DataFrame()
        ratios.index = income.index
        # Profitability Ratios
        ratios['netProfitMargin'] = income['netIncome']/income['totalRevenue']
        ratios['grossProfitMargin'] = income['grossProfit']/income['totalRevenue']
        ratios['ROA'] = income['netIncome'] / balance['totalAssets']
        ratios['ROE'] = income['netIncome'] / balance['totalShareholderEquity']
        
        #Liquidity Ratios
        ratios['currentRatio'] = balance['totalCurrentAssets']/balance['totalCurrentLiabilities']
        ratios['quickRatio'] = (balance['totalCurrentAssets'] - balance['inventory']) / balance['totalCurrentLiabilities']
        
        #Efficienct Ratios
        ratios['inventoryTurnover'] = income['costofGoodsAndServicesSold']/balance['inventory'].median()
        
        # Debt and Solvency Ratios
        ratios['debtToEquity'] = balance['shortLongTermDebtTotal']/ balance['totalShareholderEquity']
        ratios['interestCoverage'] = income['ebit'] / income['interestExpense']
        
        # Get current price of stock for the dates
        """
        Efficiency Ratios:
        Accounts Receivable Turnover: Total Credit Sales / Average Accounts Receivable
        Days Sales Outstanding (DSO): 365 / Accounts Receivable Turnover

        Price-to-Earnings (P/E) Ratio: Market Price per Share / Earnings per Share (EPS)
        Price-to-Book (P/B) Ratio: Market Price per Share / Book Value per Share
        Dividend Yield: Dividends per Share / Market Price per Share
        Earnings Yield: 12 month EPS divided by current share price
        Growth Ratios:


        Earnings Growth Rate: (Current Year's Earnings - Previous Year's Earnings) / Previous Year's Earnings
        Revenue Growth Rate: (Current Year's Revenue - Previous Year's Revenue) / Previous Year's Revenue
        Operating Efficiency Ratios:

        Operating Margin: Operating Income / Total Revenue
        Asset Turnover Ratio: Total Revenue / Average Total Assets
        Coverage Ratios:

        Debt Service Coverage Ratio: (EBITDA + Lease Payments) / Total Debt Service
        Fixed Charge Coverage Ratio: (EBIT + Lease Payments) / (Interest Expense + Lease Payments)
        Dividend Payout Ratio: Dividends Paid / Earnings

        Price-to-Sales (P/S) Ratio: Market Price per Share / Sales per Share
        price-to-book ratio: month end price divided by latest book value price
        price-to-cashflow: current price divided by most recent cash flow
        price-to-freecashflow: current price divided by most receent free cashflow
        free-cashflow-toEV
        TODO: Get price across the fiscalDateEnding and fiscaleQuarter for ongoing EPS


        """

        return ratios
