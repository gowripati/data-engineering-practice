import csv,json,os
from datetime import datetime

# Sample sales data
sales = [
  {"customer": "Alice", "product": "Pen", "price": 10, "quantity": 5},
  {"customer": "Bob", "product": "Book", "price": 100, "quantity": 2},
  {"customer": "Alice", "product": "Notebook", "price": 50, "quantity": 3},
  {"customer": "Charlie", "product": "Bag", "price": 500, "quantity": 1}
]

# Write sales data to a Json File (Extract data)

def extract(file_path, input_file):
    with open(os.path.join(file_path, input_file), "w", newline ='') as file:
        json.dump(sales, file, indent=4)

# Read sales data from Json file 

def read_json(file_path, input_file):
    with open(os.path.join(file_path, input_file), "r") as v2:
        data = json.load(v2)
    return data

# Transform data

def transform(file_path, input_file):
    var1 = read_json(file_path, input_file)
    customer_summary = {}
    for entry in var1:
        if entry["customer"] not in customer_summary:
            customer_summary[entry["customer"]] = entry["price"] * entry["quantity"]
        else:
            customer_summary[entry["customer"]] += entry["price"] * entry["quantity"]
    return customer_summary

# Load data to CSV file

def load(file_path, file_name, summary_data):
    output_path = os.path.join(file_path, file_name)
    with open(output_path, "w", newline='') as file2:
        writer = csv.writer(file2)
        writer.writerow(["Customer", "Total Revenue"])
        for customer, revenue in summary_data.items():
            writer.writerow([customer, revenue])

# Log metadata (write to text file)

def log_metadata(file_path, summary_data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rows_processed = len(sales)
    log_entry = f"{timestamp} | Rows processed: {rows_processed} | Customers: {len(summary_data)}\n"
    text_path = os.path.join(file_path, "run_log.txt")
    with open(text_path, "a") as log:
        log.write(log_entry)


if __name__ == "__main__":
    file_path = "C:\\Users\\gowri\\Documents\\Projects\\Day_3\\"
    input_file = "sales1.json"
    output_file = "customer_revenue.csv"

    extract(file_path, input_file)
    summary = transform(file_path, input_file)
    load(file_path, output_file, summary)
    log_metadata(file_path, summary)

    print("ETL pipeline completed successfully!")