import pandas as pd
import numpy as np

import functionTool as ft
from alpha_vantage.timeseries import TimeSeries

api = "B9BL0WND53Q9UY0H"
ts = TimeSeries(api, output_format="pandas")
output_folder = r"C:\Users\chenr\OneDrive\Desktop\Pythons\Output"

#class, string date, string date, "monthly"/"weekly"
class security_data():
    def __init__(self, symbol, start, end, freq):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.freq = freq

        if(freq == "weekly"):
            raw_data, raw_info = ts.get_weekly(self.symbol)
            self.data = ft.modify_df(raw_data, start, end)
        elif(freq == "monthly"):
            raw_data, raw_info = ts.get_monthly(self.symbol)
            self.data = ft.modify_df(raw_data, start, end)
        else:
            print("Error")
    #
    def get_info_list(self):
        return [self.symbol, self.start, self.end, self.freq]
    
    #get percentage change table on prices, remove the first row
    def get_return_data(self):
        df = pd.DataFrame(self.data)
        df_price = df.loc[:,"Open":"Close"]
        print(df_price)
        df_volume = df.loc[:,"Volume"]
        df_return = df_price.pct_change()
        df_merged = pd.merge(df_return, df_volume, on = "date")
        return df_merged.iloc[1:,:]
    
    #create pirce date csv file in the given folder
    def price_to_csv(self, output_folder):
        if(self.freq == "weekly"):
            ft.wkly_to_csv(output_folder, self.data, self.symbol, self.start, self.end)
        elif(self.freq == "monthly"):
            ft.mly_to_csv(output_folder, self.data, self.symbol, self.start, self.end)
        
MSFT = security_data("MSFT", "1900-01-01","2023-02-13", "monthly")


#print(MSFT.data[["Open","High","Low","Close"]])
#print(MSFT.data.loc[:,'Open':'Close'])

print(MSFT.get_return_data())
MSFT.price_to_csv(output_folder)


        
        
