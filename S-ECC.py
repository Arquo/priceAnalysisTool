import pandas as pd
import requests 
import functionTool as ft 

api = "B9BL0WND53Q9UY0H"
api2 = "DOBGJDVX5NOEA98X"

class Security:
    def __init__(self, symbol, start, end, frequence, api):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.frequence = frequence
        self.api = api
    
class Equity(Security):
    def __init__(self, symbol, start, end, frequence, api):
        super().__init__(symbol, start, end, frequence, api)
        self.data = ft.requestEquity(self.symbol,self.start,self.end,self.frequence,self.api)

class Cypto(Security):
    def __init__(self, symbol, start, end, frequence, api):
        super().__init__(symbol, start, end, frequence, api)
        df  = ft.requestCrypto(self.symbol,self.start,self.end,self.frequence,self.api,"USD")
        self.data = df.drop(df.iloc[:,[1,3,5,7]], axis = 1)
        self.data.columns =  ["1. open (USD)", "2. high (USD)", 
                              "3. low (USD)", "4. close (USD)", 
                              "5. volume", "6. market cap (USD)"]
    def get_data_in_currency(self, in_currency):
        df  = ft.requestCrypto(self.symbol,self.start,self.end,self.frequence,self.api, in_currency)
        df = df.drop(df.iloc[:,[1,3,5,7]], axis = 1)
        df = pd.DataFrame(df)
        df.columns = ["1. open ("+in_currency+")", "2. high ("+in_currency+")", 
                      "3. low ("+in_currency+")", "4. close ("+in_currency+")", 
                      "5. volume", "6. market cap (USD)"]
        return df

#NATURAL_GAS, BRENT, WTI
class Commodity(Security):
    
    def getdata(self):
        return ft.requestComm(self.symbol, self.start, self.end, self.frequence, self.api)
    
    
    

TSLA = Equity ("TSLA", "2022-03-23", "2023-01-23","monthly",api)
print(TSLA.data)

#BTC = Cypto("BTC", "2022-03-23", "2023-01-23","monthly",api)
#print(BTC.get_data_in_currency("CNY"))

BRENT = Commodity("BRENT", "2022-03-23", "2023-01-23","monthly",api)
print(BRENT.getdata())
















