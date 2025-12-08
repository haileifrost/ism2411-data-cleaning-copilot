# data_cleaning.py
# This script loads raw sales data, applies standard data cleaning steps,
# and outputs the cleaned data for further analysis.

import pandas as pd

# Function to load data from a CSV file into a pandas DataFrame.
# Should handle missing file errors gracefully and return a DataFrame.
def load_data(file_path: str):
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded data from {file_path}, shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return pd.DataFrame()

# Function to standardize and clean column names in a DataFrame.
# Should make names lowercase, strip whitespace, and replace spaces with underscores.
def clean_column_names(df):
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    print("Column names standardized.")
    return df

# Function to handle missing values in price and quantity columns.
# Should convert to numeric and fill missing values with zero for consistency.
def handle_missing_values(df):
    for field in ['price', 'quantity']:
        if field in df.columns:
            df[field] = pd.to_numeric(df[field], errors='coerce').fillna(0)
    print("Missing values handled.")
    return df

# Function to remove rows with negative price or quantity.
# Should filter out invalid entries where either value is less than zero.
def remove_invalid_rows(df):
    for field in ['price', 'quantity']:
        if field in df.columns:
            df = df[df[field] >= 0]
    print("Invalid rows removed.")
    return df

def main():
    raw_path = 'data/raw/sales_data_raw.csv'
    processed_path = 'data/processed/sales_data_clean.csv'

    # Load and process data step by step
    df = load_data(raw_path)
    df = clean_column_names(df)

    # Clean up product/category whitespace
    if 'product' in df.columns:
        df['product'] = df['product'].str.strip()
    if 'category' in df.columns:
        df['category'] = df['category'].str.strip()

    df = handle_missing_values(df)
    df = remove_invalid_rows(df)

    df.to_csv(processed_path, index=False)
    print(f"Cleaned data written to {processed_path}")
    if __name__ == "__main__":
        raw_path = "data/raw/sales_data_raw.csv"
        cleaned_path = "data/processed/sales_data_clean.csv"
# Copied and pasted from assignment requirements to ensure that the code works properly as intended.
        df_raw = load_data(raw_path)
        df_clean = clean_column_names(df_raw)
        df_clean = handle_missing_values(df_clean)
        df_clean = remove_invalid_rows(df_clean)
        df_clean.to_csv(cleaned_path, index=False)
        print("Cleaning complete. First few rows:")
        print(df_clean.head())
