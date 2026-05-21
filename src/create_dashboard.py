import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import os

# 1. Connect to our SQL Warehouse
conn = sqlite3.connect('exchange_warehouse.db')

# 2. Get the Top 5 currencies for the chart
query = "SELECT currency, AVG(rate) as avg_rate FROM currency_rates GROUP BY currency ORDER BY avg_rate DESC LIMIT 5"
df = pd.read_sql_query(query, conn)

# 3. Create the Plot
plt.figure(figsize=(10, 6))
plt.bar(df['currency'], df['avg_rate'], color='skyblue')
plt.title('Top 5 Most Valuable Currencies (USD Base)')
plt.ylabel('Exchange Rate')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 4. Save the chart to a 'reports' folder
os.makedirs('reports', exist_ok=True)
plt.savefig('reports/currency_trends.png')
print("✅ Dashboard chart generated in /reports/currency_trends.png")
