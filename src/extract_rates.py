import pandas as pd
import requests
import os
from datetime import datetime

class RateExtractor:
    def __init__(self):
        self.output_dir = 'data'
        self.api_url = "https://api.exchangerate-api.com/v4/latest/USD"

    def run(self):
        # 1. Extract
        response = requests.get(self.api_url)
        data = response.json()
        
        # 2. Transform
        rates = data['rates']
        df = pd.DataFrame(list(rates.items()), columns=['currency', 'rate'])
        df['timestamp'] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        # 3. Load
        os.makedirs(self.output_dir, exist_ok=True)
        date_str = datetime.utcnow().strftime("%Y-%m-%d")
        file_path = os.path.join(self.output_dir, f"rates_{date_str}.csv")
        
        df.to_csv(file_path, index=False)
        print(f"✅ Data successfully loaded to: {file_path}")
        print(f"📂 Current files in {self.output_dir}: {os.listdir(self.output_dir)}")

if __name__ == "__main__":
    extractor = RateExtractor()
    extractor.run()
