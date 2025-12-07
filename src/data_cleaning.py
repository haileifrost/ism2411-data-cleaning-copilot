import pandas as pd

def clean_sales_data():
    df = pd.read_csv('data/raw/sales_data_raw.csv')
    # Simple cleaning: filter out rows where sale_amount is not a number
    df['sale_amount'] = pd.to_numeric(df['sale_amount'], errors='coerce')
    df_clean = df.dropna()
    df_clean.to_csv('data/processed/sales_data_clean.csv', index=False)

if __name__ == "__main__":
    clean_sales_data()
