import pandas as pd

def clean_sales_data(df):
    df = df.drop_duplicates()
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Revenue'] = df['Revenue'].fillna(0)
    df['Profit'] = df['Profit'].fillna(0)
    df['Profit_Margin'] = (df['Profit'] / df['Revenue'].replace(0,1)) * 100
    df['Profit_Margin'] = df['Profit_Margin'].round(2)
    return df 

