print("utils.py loaded successfully")

import pandas as pd

def clean_column_names(df):
    """
    Cleans dataframe column names.
    - Removes spaces
    - Converts to lowercase
    - Replaces spaces with underscores
    """
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df
