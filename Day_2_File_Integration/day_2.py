import csv,json
from datetime import datetime

# Sample sales data
sales = [
  {"customer": "Alice", "product": "Pen", "price": 10, "quantity": 5},
  {"customer": "Bob", "product": "Book", "price": 100, "quantity": 2},
  {"customer": "Alice", "product": "Notebook", "price": 50, "quantity": 3},
  {"customer": "Charlie", "product": "Bag", "price": 500, "quantity": 1}
]

# Write sales data to a JSON file (Extract data)

file_path = "C:\\Users\\gowri\\Documents\\Projects\\Day_2_File_Integration\\sales.json"
with open(file_path, "w", newline='') as file:
    json.dump(sales, file, indent=4)

with open(file_path, "r") as v2:
    data = json.load(v2)

# Calculate total revenue per customer (Transform data)

customer_summary = {}
for entry in data:
    if entry["customer"] not in customer_summary:
        customer_summary[entry["customer"]] = entry["price"] * entry["quantity"]
    else:
        customer_summary[entry["customer"]] += entry["price"] * entry["quantity"]

# Write customer revenue summary to a CSV file (Load data)

output_path = "C:\\Users\\gowri\\Documents\\Projects\\Day_2_File_Integration\\customer_revenue.csv"
with open(output_path, "w", newline='') as file2:
    writer = csv.writer(file2)
    writer.writerow(["Customer", "Total Revenue"])
    for customer, revenue in customer_summary.items():
        writer.writerow([customer, revenue])

# ✅ Step 4 - Log metadata (write to text file)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
rows_processed = len(sales)
log_entry = f"{timestamp} | Rows processed: {rows_processed} | Customers: {len(customer_summary)}\n"

text_path = "C:\\Users\\gowri\\Documents\\Projects\\Day_2_File_Integration\\run_log.txt"
with open(text_path, "a") as log:
    log.write(log_entry)

print("ETL pipeline completed successfully!")



