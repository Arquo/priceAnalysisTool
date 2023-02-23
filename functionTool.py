import os
import numpy as np
import pandas as pd
import requests


#dataframe, string date, string date
def modify_df(df, start, end):
        df = pd.DataFrame(df)
        df = df.sort_index()
        return df.loc[start:end]

def get_return_data(price_data):
    df = pd.DataFrame(price_data)
    df_price = df.iloc[:,0:5]
    df_others = df.iloc[:,5:7]
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
    df_change = (price_data).pct_change().iloc[:,4]
    data_change_std = np.std(df_change)
    annualized_std = 0
    if(freq == "weekly"):
        annualized_std = data_change_std * np.sqrt(52)
    elif(freq == "monthly"):
        annualized_std = data_change_std * np.sqrt(12) 
    return annualized_std


#############################################################################
def requestEquity(symbol, start, end, frequence, api):
    function = ""
    if(frequence == "daily"):
        function = "TIME_SERIES_DAILY_ADJUSTED"
    elif(frequence == "weekly"):
        function = "TIME_SERIES_WEEKLY_ADJUSTED"
    elif(frequence == "monthly"):
        function = "TIME_SERIES_MONTHLY_ADJUSTED"
    url = "https://www.alphavantage.co/query?function="+function+"&symbol="+symbol+"&apikey=+"+api
    
    dictionary = requests.get(url).json()
    df = []
    if(frequence == "daily"):
        df = dictionary["Time Series (Daily)"]
    elif(frequence == "weekly"):
        df = dictionary["Weekly Adjusted Time Series"]   
    elif(frequence == "monthly"):
        df = dictionary["Monthly Adjusted Time Series"]   
    
    df = pd.DataFrame(df)
    return modify_df(df.transpose(), start, end)
    
def requestCrypto(symbol, start, end, frequence, api, to_currency):
    function = ""
    if(frequence == "daily"):
        function = "DIGITAL_CURRENCY_DAILY"
    elif(frequence == "weekly"):
        function = "DIGITAL_CURRENCY_WEEKLY"
    elif(frequence == "monthly"):
        function = "DIGITAL_CURRENCY_MONTHLY"
    url = "https://www.alphavantage.co/query?function="+function+"&symbol="+symbol+"&market="+to_currency+"&apikey=+"+api   
    
    dictionary = requests.get(url).json()
    df = []
    if(frequence == "daily"):
        df = dictionary["Time Series (Digital Currency Daily)"]
    elif(frequence == "weekly"):
        df = dictionary["Time Series (Digital Currency Weekly)"]   
    elif(frequence == "monthly"):
        df = dictionary["Time Series (Digital Currency Monthly)"]   
    
    df = pd.DataFrame(df)
    return modify_df(df.transpose(), start, end)

def requestComm(symbol, start, end, frequence, api):
    url = "https://www.alphavantage.co/query?function="+symbol+"&interval="+frequence+"&apikey="+api
    dictionary = requests.get(url).json()
    df = dictionary["data"]
    df = pd.DataFrame(df)
    return modify_df(df.set_index("date"), start, end)


def find_stat(symbol):
    if(type(symbol) == ss.Equity):
        print("yes")
