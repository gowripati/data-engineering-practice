import pandas as pd
import logging

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the column names of a DataFrame by stripping whitespace,
    lowering case, and replacing spaces with underscores."""

    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df


def read_csv_file(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
        logging.info(f"✅ Successfully read file: {file_path} (rows: {len(df)})")
        return df
    except FileNotFoundError:
        logging.error(f"❌ File not found: {file_path}")
        return pd.DataFrame()
    except pd.errors.EmptyDataError:
        logging.error(f"⚠️ File is empty: {file_path}")
        return pd.DataFrame()
    except Exception as e:
        logging.error(f"❌ Error reading {file_path}: {e}")
        return pd.DataFrame()