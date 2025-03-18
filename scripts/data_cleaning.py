import pandas as pd
import sqlite3
import os

# Constants
FILE_PATH = r"C:\Users\Hp\Documents\customer_behavior_analysis\data\shopping_trends.csv"
SAVE_FOLDER = r"C:\Users\Hp\Documents\customer_behavior_analysis\data"
CSV_FILE_PATH = rf"{SAVE_FOLDER}\shopping_trends_cleaned.csv"
EXCEL_FILE_PATH = rf"{SAVE_FOLDER}\shopping_trends_cleaned.xlsx"
DB_FILE_PATH = rf"{SAVE_FOLDER}\shopping_trends.db"

def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path)

def display_data_info(df):
    """Display the first 5 rows and data types of each column."""
    print(df.head())
    print("Column Data Types:\n", df.dtypes)

def standardize_column_names(df):
    """Standardize column names by stripping, lowering case, and replacing spaces with underscores."""
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

def check_missing_values(df):
    """Check for missing values in the dataset."""
    missing_values = df.isnull().sum()
    print("Missing Values:\n", missing_values)

def check_duplicates(df):
    """Check for duplicate rows in the dataset."""
    duplicate_count = df.duplicated().sum()
    print(f"Duplicate Rows: {duplicate_count}")

def save_data(df, csv_file_path, excel_file_path, db_file_path):
    """Save the cleaned data to CSV, Excel, and SQLite Database."""
    # Ensure the directory exists before saving
    os.makedirs(SAVE_FOLDER, exist_ok=True)

    # Save as CSV
    df.to_csv(csv_file_path, index=False)

    # Save as Excel
    df.to_excel(excel_file_path, index=False)

    # Save as SQLite Database
    conn = sqlite3.connect(db_file_path)
    df.to_sql("shopping_trends", conn, if_exists="replace", index=False)
    conn.close()

    print("✅ Data successfully saved as CSV, Excel, and SQLite Database.")

def run():
    """Main function to run the data cleaning process."""
    # Load the dataset
    df = load_data(FILE_PATH)

    # Display data information
    display_data_info(df)

    # Standardize column names
    standardize_column_names(df)

    # Check for missing values
    check_missing_values(df)

    # Check for duplicates
    check_duplicates(df)

    # Save the cleaned data
    save_data(df, CSV_FILE_PATH, EXCEL_FILE_PATH, DB_FILE_PATH)

# Run the script when executed
if __name__ == "__main__":
    run()