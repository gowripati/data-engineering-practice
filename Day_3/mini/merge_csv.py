# merge_csvs.py
import os
import pandas as pd
import logging
from utils import clean_column_names, read_csv_file

print("Current working directory:", os.getcwd())
# ---------------------------------------------
# 1️⃣ Setup Logging
# ---------------------------------------------

LOG_DIR = r"C:\Users\gowri\Documents\Projects\Day_3\mini"
LOG_FILE = os.path.join(LOG_DIR, "merge_log.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()  # Optional: also log to console
    ]
)

logging.info("🚀 Script started: Merging multiple CSVs")

# ---------------------------------------------
# 2️⃣ Define Directories
# ---------------------------------------------
DATA_DIR = r"C:\Users\gowri\Documents\Projects\Day_3\mini\data"
OUTPUT_FILE = r"C:\Users\gowri\Documents\Projects\Day_3\mini\merged_sales.csv"

# ---------------------------------------------
# 3️⃣ Core Logic
# ---------------------------------------------
def merge_csv_files(data_dir: str, output_file: str):
    merged_df = pd.DataFrame()

    try:
        csv_files = [f for f in os.listdir(data_dir) if f.endswith(".csv")]
        if not csv_files:
            logging.warning("⚠️ No CSV files found in the data folder.")
            print("No CSV files found!")
            return

        for file in csv_files:
            file_path = os.path.join(data_dir, file)
            logging.info(f"Reading file: {file_path}")

            df = read_csv_file(file_path)
            if df.empty:
                continue

            # Clean and filter
            df = clean_column_names(df)
            df.dropna(subset=["amount"], inplace=True)

            merged_df = pd.concat([merged_df, df], ignore_index=True)

        # Save merged data
        merged_df.to_csv(output_file, index=False)
        logging.info(f"✅ Final merged file saved as {output_file}")
        print(f"✅ Merged file created: {output_file}")

    except Exception as e:
        logging.error(f"❌ Unexpected error during merge: {e}")
        print("Error:", e)


# ---------------------------------------------
# 4️⃣ Run the Script
# ---------------------------------------------
if __name__ == "__main__":
    merge_csv_files(DATA_DIR, OUTPUT_FILE)
    logging.info("🏁 Script completed successfully")