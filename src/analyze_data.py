import pandas as pd
import sqlite3
import os
import glob

# 1. Setup paths relative to this script
# This ensures it works on your laptop AND on GitHub
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
data_folder = os.path.join(project_root, 'data')
pattern = os.path.join(data_folder, '*.csv')

# 2. Connect to SQL
conn = sqlite3.connect('exchange_warehouse.db')

# 3. Load files
all_files = glob.glob(pattern)

if not all_files:
    print(f"❌ Error: No CSV files found in {data_folder}")
    print(f"Checking path: {pattern}")
else:
    df_list = [pd.read_csv(f) for f in all_files]
    master_df = pd.concat(df_list, ignore_index=True)
    master_df.to_sql('currency_rates', conn, if_exists='replace', index=False)

    # 4. SQL Analysis
    query = """
    SELECT 
        currency,
        ROUND(AVG(rate), 4) as avg_rate,
        ROUND(MAX(rate) - MIN(rate), 4) as volatility
    FROM currency_rates
    GROUP BY currency
    ORDER BY avg_rate DESC
    LIMIT 10
    """
    
    results = pd.read_sql_query(query, conn)
    print("\n📊 --- TOP 10 CURRENCIES BY VALUE (SQL) ---")
    print(results)
    
    conn.close()
