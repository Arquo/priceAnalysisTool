import pandas as pd
import numpy as np
import functionTool as ft
from alpha_vantage.timeseries import TimeSeries

api = "B9BL0WND53Q9UY0H"
api2 = "DOBGJDVX5NOEA98X"
ts = TimeSeries(api2, output_format="pandas")
output_folder = r"C:\Users\chenr\OneDrive\Desktop\Pythons\Output"

#class, string date, string date, "monthly"/"weekly"
#monthly data avaliable from 
class security_data():
    def __init__(self, symbol, start, end, freq):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.freq = freq

        if(freq == "weekly"):
            raw_data, raw_info = ts.get_weekly_adjusted(self.symbol)
            self.price_data = ft.modify_df(raw_data, start, end)
        elif(freq == "monthly"):
            raw_data, raw_info = ts.get_monthly_adjusted(self.symbol)
            self.price_data = ft.modify_df(raw_data, start, end)
        else:
            print("Error")
    #
    def get_info_list(self):
        return [self.symbol, self.start, self.end, self.freq]
    
    #get percentage change table on prices, remove the first row
    def get_return_data(self):
        return ft.get_return_data(self.price_data)
    
    #create pirce date csv file in the given folder
    def price_to_csv(self, output_folder):
        ft.df_to_csv(output_folder, self.price_data, self.symbol, self.start, self.end, self.freq)
    
    #Using adjusted price
    def period_statistics(self):
        annualized_return= ft.find_annual_return(self.price_data, self.freq)
        annualized_std = ft.find_annual_vol(self.price_data, self.freq)
        return [annualized_return, annualized_std]
    



MSFT1 = security_data("MSFT", "2000-12-31","2023-01-31", "weekly")
print(MSFT1.price_data)
print(MSFT1.get_return_data())
print(MSFT1.period_statistics())









   
        
        
        
