import pandas as pd
import sqlite3
import os
import glob

# 1. Connect to a local SQL database (This creates the file if it doesn't exist)
conn = sqlite3.connect('exchange_warehouse.db')

# 2. Find all daily CSVs in your data folder
path = './data/*.csv'
print(f"Checking for files in: {os.path.abspath(path)}")
all_files = glob.glob(path)

if not all_files:
    print("No data found to analyze! Please run the extraction script first.")
else:
    # Combine all individual daily files into one Master DataFrame
    df_list = [pd.read_csv(f) for f in all_files]
    master_df = pd.concat(df_list, ignore_index=True)
    
    # Push the data into a SQL table named 'currency_rates'
    master_df.to_sql('currency_rates', conn, if_exists='replace', index=False)

    # 3. THE SQL ENGINE: Run a professional analytical query
    # We are calculating average rates and volatility (max price - min price)
    query = """
    SELECT 
        currency,
        AVG(rate) as average_rate,
        MAX(rate) - MIN(rate) as volatility
    FROM currency_rates
    GROUP BY currency
    ORDER BY volatility DESC
    """
    
    results = pd.read_sql_query(query, conn)
    
    print("\n--- SQL ANALYSIS RESULTS ---")
    print(results)
    
    # Close the connection
    conn.close()
