import pandas as pd
import numpy as np
import os
from alpha_vantage.timeseries import TimeSeries

api = "B9BL0WND53Q9UY0H"
ts = TimeSeries(api, output_format="pandas")

def modify_df(df):
        df = pd.DataFrame(df)
        df = df.sort_index()
        df.columns= ["Open", "High","Low","Close","Volume"]
        return df
        
class security():
    def __init__(self, symbol):
        self.symbol = symbol
        
    def get_weekly_data(self, start, end):
        self.weekly_data, self.weekly_info = ts.get_weekly(self.symbol)
        period_df = modify_df(self.weekly_data).loc[start:end]

        file_name = self.symbol + "~"+ start + "~" + end + ".csv"
        path = os.path.join(r"C:\Users\chenr\OneDrive\Desktop\Pythons\Output", file_name)
        period_df.to_csv(path)
        return period_df

MSFT = security("AAPL")
file = MSFT.get_weekly_data("2023-01-06","2023-02-10")
print(file)








   
        
        
        