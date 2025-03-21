import pandas as pd
import os

# Paths
FILE_PATH = r"C:\Users\Hp\Documents\customer_behavior_analysis\data\shopping_trends.csv"
CLEANED_DATA_PATH = r"C:\Users\Hp\Documents\customer_behavior_analysis\data\shopping_trends_cleaned.csv"

def clean_data():
    """Loads raw data, performs cleaning, and saves cleaned data."""
    
    if not os.path.exists(FILE_PATH):
        raise FileNotFoundError(f"❌ Raw data file not found: {FILE_PATH}")

    print(f"📂 Loading raw data from {FILE_PATH}...")
    df = pd.read_csv(FILE_PATH)

    # Example cleaning: remove missing values
    df.dropna(inplace=True)

    # Save cleaned data
    df.to_csv(CLEANED_DATA_PATH, index=False)
    print(f"✅ Cleaned data saved at {CLEANED_DATA_PATH}")

if __name__ == "__main__":
    clean_data()
