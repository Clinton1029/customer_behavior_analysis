import os
import pandas as pd
import eda, insights, data_visualization  # Ensure modules exist

# Paths to cleaned files
CLEANED_CSV = "data/shopping_trends_cleaned.csv"
CLEANED_EXCEL = "data/shopping_trends_cleaned.xlsx"
CLEANED_DB = "data/shopping_trends.db"

def check_cleaned_data_exists():
    """Check if cleaned data already exists before running data cleaning."""
    return all(os.path.exists(f) for f in [CLEANED_CSV, CLEANED_EXCEL, CLEANED_DB])

def main():
    """Main function to orchestrate EDA, insights, visualizations, and data cleaning (if needed)."""
    print("\n🔍 Running Exploratory Data Analysis (EDA)...")
    eda.run()

    print("\n📊 Running insights module...")
    insights.run()

    print("\n📈 Running visualization module...")
    data_visualization.run()

    if not check_cleaned_data_exists():
        print("\n🔹 Running data cleaning (since cleaned files do not exist)...")
        from scripts import data_cleaning  # Import only if needed
        data_cleaning.clean_data()
    else:
        print("\n✅ Cleaned data already exists. Skipping data cleaning.")

if __name__ == "__main__":
    main()
