import pandas as pd
from data_tools.utils import clean_column_names
from data_tools.db_utils import connect_to_db

# Sample DataFrame
data = {
    " Product Name ": ["Laptop", "Keyboard", "Mouse"],
    " Sale Amount ": [1000, 500, 200]
}
df = pd.DataFrame(data)

# Use function from utils.py
df = clean_column_names(df)
print(df.columns)

# Use function from db_utils.py
conn = connect_to_db("sales.db")
conn.close()
