import os
import pandas as pd
from scripts import insights, visualization  # Ensure these modules exist
# from scripts import data_cleaning  # Uncomment only if cleaning should be forced

# Paths to cleaned files
CLEANED_CSV = "data/shopping_trends_cleaned.csv"
CLEANED_EXCEL = "data/shopping_trends_cleaned.xlsx"
CLEANED_DB = "data/shopping_trends.db"

def check_cleaned_data_exists():
    """Check if cleaned data already exists before running data cleaning."""
    return os.path.exists(CLEANED_CSV) and os.path.exists(CLEANED_EXCEL) and os.path.exists(CLEANED_DB)

def main():
    """Main function to orchestrate data processing and analysis."""
    if not check_cleaned_data_exists():
        print("🔹 Running data cleaning...")
        from scripts import data_cleaning  # Run cleaning only when needed
        data_cleaning.clean_data()  # Ensure `clean_data()` exists in data_cleaning.py
    else:
        print("✅ Cleaned data already exists. Skipping data cleaning.")

    print("📊 Running insights module...")
    insights.run()

    print("📈 Running visualization module...")
    visualization.run()

if __name__ == "__main__":
    main()
