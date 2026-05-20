# 📈 Automated Currency Exchange Rate Pipeline

A production-ready ETL pipeline that automatically tracks cryptocurrency and fiat exchange rates daily.

## 🚀 Project Overview
This project automates the collection of financial data using Python and GitHub Actions. It eliminates manual data entry by fetching real-time rates and storing them in a structured CSV "Data Lake."

## 🛠️ Tech Stack
* **Language:** Python 3.9
* **Libraries:** Pandas, Requests
* **Automation:** GitHub Actions (CI/CD)
* **Storage:** CSV / Git

## 🔄 How It Works
1. **Extract:** A Python script connects to the Exchange Rate API.
2. **Transform:** Data is cleaned and formatted into a time-stamped CSV using Pandas.
3. **Load:** GitHub Actions triggers every midnight (UTC), creates a `/data` directory, and commits the new file to this repository.

## 📁 Repository Structure
* `/src`: Contains the Python extraction logic.
* `/data`: Automated storage for daily exchange rate CSVs.
* `/.github/workflows`: The YAML configuration for the daily automation.
