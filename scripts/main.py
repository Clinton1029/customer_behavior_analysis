import os
import pandas as pd

# Paths
RAW_DATA_PATH = r"C:\Users\Hp\Documents\customer_behavior_analysis\data\shopping_trends.csv"
CLEANED_CSV = r"C:\Users\Hp\Documents\customer_behavior_analysis\data\shopping_trends_cleaned.csv"

def check_cleaned_data_exists():
    """Check if cleaned data exists before proceeding."""
    return os.path.exists(CLEANED_CSV)

def main():
    """Main execution flow."""

    if not check_cleaned_data_exists():
        print("\n🔹 Cleaned data missing. Running data cleaning first...")

        # Ensure raw data exists before running cleaning
        if not os.path.exists(RAW_DATA_PATH):
            raise FileNotFoundError(f"❌ Raw dataset not found: {RAW_DATA_PATH}")

        import data_cleaning  # Ensure this file exists!

        # Ensure the cleaning function exists
        if hasattr(data_cleaning, "clean_data"):
            data_cleaning.clean_data()
        else:
            raise AttributeError("❌ No valid data cleaning function found in data_cleaning.py!")

        print("\n✅ Data cleaning completed and saved.")
    else:
        print("\n✅ Cleaned data already exists. Skipping data cleaning.")

    # Ensure cleaned data exists before running analysis
    if not os.path.exists(CLEANED_CSV):
        raise FileNotFoundError(f"❌ Cleaned dataset not found at: {CLEANED_CSV}. Data cleaning may have failed.")

    # Now import analysis modules
    import eda, insights, data_visualization  

    print("\n🔍 Running Exploratory Data Analysis (EDA)...")
    eda.run()

    print("\n📊 Running insights module...")
    insights.run()

    print("\n📈 Running visualization module...")
    data_visualization.run()

if __name__ == "__main__":
    main()
