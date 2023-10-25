import pandas as pd 
import io 
import requests

class vantageBase():
    
    def __init__(self):
        self.url = 'https://www.alphavantage.co/query?'
        self.apikey = 'QZ2N93YNOQE6LALE'
        self.apistr = f'apikey={self.apikey}'
        self.datatype = 'datatype=csv'

    def getData(self, url) -> pd.DataFrame:
        r = requests.get(url)
        r = r.content
        rawData = pd.read_csv(io.StringIO(r.decode('utf-8')))
        return rawData

    def getJson(self, url) -> dict:
        r = requests.get(url)
        data = r.json()
        return data

