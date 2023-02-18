import os
import pandas as pd


#dataframe, string date, string date
def modify_df(df, start, end):
        df = pd.DataFrame(df)
        df = df.sort_index()
        df.columns= ["Open", "High","Low","Close","Volume"]
        return df.loc[start:end]

#folder path, dataframe, string, string date, string date
def wkly_to_csv(output_folder, df, symbol, start, end):
    file_name = symbol + "~wkly~"+ start + "~" + end + ".csv"
    path = os.path.join(output_folder, file_name)
    df.to_csv(path)
    
    #folder path, dataframe, string, string date, string date
def mly_to_csv(output_folder, df, symbol, start, end):
    file_name = symbol + "~mly~"+ start + "~" + end + ".csv"
    path = os.path.join(output_folder, file_name)
    df.to_csv(path)