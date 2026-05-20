def load_data(self, df):
        """Loads the transformed dataframe into a local CSV storage file."""
        if df is None or df.empty:
            print("No data to load.")
            return

        # Explicitly create the directory if it doesn't exist
        # This is a common point of failure in automated environments!
        os.makedirs(self.output_dir, exist_ok=True)
        
        date_str = datetime.datetime.utcnow().strftime("%Y-%m-%d")
        file_path = os.path.join(self.output_dir, f"rates_{date_str}.csv")
        
        df.to_csv(file_path, index=False)
        print(f"Data successfully loaded to: {file_path}")
        
        # Professional check: Print the directory contents to confirm success in logs
        print(f"Current files in {self.output_dir}: {os.listdir(self.output_dir)}")
