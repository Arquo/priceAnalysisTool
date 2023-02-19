import os
import numpy as np
import pandas as pd


#dataframe, string date, string date
def modify_df(df, start, end):
        df = pd.DataFrame(df)
        df = df.sort_index()
        df.columns= ["Open", "High","Low","Close","Adjusted Close","Volume","Dividend Amount"]
        return df.loc[start:end]

def get_return_data(price_data):
    df = pd.DataFrame(price_data)
    df_price = df.loc[:,"Open":"Adjusted Close"]
    df_others = df.loc[:,"Volume":"Dividend Amount"]
    df_change = df_price.pct_change()
    df_merged = pd.merge(df_change, df_others, on = "date")
    return df_merged.iloc[1:,:]


def df_to_csv(output_folder, df, symbol, start, end, freq): 
    file_name = symbol + "~" + freq + "~" + start + "~" + end + ".csv"
    path = os.path.join(output_folder, file_name)
    df.to_csv(path)

def find_annual_return(price_data, freq):
    start_price = price_data.iloc[0,4] 
    end_price = price_data.iloc[-1,4] 
    num_row = price_data.shape[0]
      #annualized_return
    annualized_return = 0
    if(freq == "weekly"):
        annualized_return = pow(end_price/start_price, 52/(num_row - 1)) - 1
    elif(freq == "monthly"):
        annualized_return = pow(end_price/start_price, 12/(num_row - 1)) - 1
    return annualized_return

def find_annual_vol(price_data, freq):
    df_change = (price_data).pct_change().loc[:,"Adjusted Close"]
    data_change_std = np.std(df_change)
    annualized_std = 0
    if(freq == "weekly"):
        annualized_std = data_change_std * np.sqrt(52)
    elif(freq == "monthly"):
        annualized_std = data_change_std * np.sqrt(12) 
    return annualized_std
            
            
   
