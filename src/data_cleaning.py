# data_cleaning.py
# This script loads raw sales data, applies standard data cleaning steps,
# and outputs the cleaned data for further analysis.

import pandas as pd

# Load the raw sales data
# Source: data/raw/sales_data_raw.csv
raw_path = 'data/raw/sales_data_raw.csv'
processed_path = 'data/processed/sales_data_clean.csv'
df = pd.read_csv(raw_path)

# Standardize column names
# Why: Consistent column names simplify downstream analysis and automation
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Clean up product and category columns
# What: Strip leading/trailing spaces
# Why: Prevent mismatches due to accidental whitespace
if 'product' in df.columns:
    df['product'] = df['product'].str.strip()
if 'category' in df.columns:
    df['category'] = df['category'].str.strip()

# Handle missing prices and quantities
# What: Fill missing with zeros
# Why: We want a consistent policy; using 0 avoids dropping too much data
for field in ['price', 'quantity']:
    if field in df.columns:
        df[field] = pd.to_numeric(df[field], errors='coerce').fillna(0)

# Remove rows with negative quantity or negative price
# What: Drop rows with negative values
# Why: Negative values are likely data entry errors and invalid for analysis
for field in ['price', 'quantity']:
    if field in df.columns:
        df = df[df[field] >= 0]

# Save the cleaned data to processed file
df.to_csv(processed_path, index=False)
print(f"Cleaned data written to {processed_path}")
