import pandas as pd
from utils import clean_sales_data

df = pd.read_csv(r"C:\Users\gowri\Documents\Projects\Day_5\Data\raw_sales.csv")

# clean the data

df = clean_sales_data(df)

# Step 3: Summary Reports
region_summary = df.groupby('Region')[['Revenue', 'Profit']].sum().reset_index()
product_summary = df.groupby('Product')[['Revenue', 'Profit']].sum().reset_index()

# Step 4: Pivot Table (Dashboard)
pivot = pd.pivot_table(
    df,
    values='Revenue',
    index='Region',
    columns='Product',
    aggfunc='sum',
    fill_value=0
)

# Step 5: Output Results
print("\n📊 Region Summary:\n", region_summary)
print("\n🛒 Product Summary:\n", product_summary)
print("\n📈 Pivot Dashboard:\n", pivot)

# Optional: Save outputs
region_summary.to_csv(r"C:\Users\gowri\Documents\Projects\Day_5\Data\region_summary.csv", index=False)
product_summary.to_csv(r'C:\Users\gowri\Documents\Projects\Day_5\Data\product_summary.csv', index=False)
pivot.to_csv(r'C:\Users\gowri\Documents\Projects\Day_5\Data\pivot_dashboard.csv')