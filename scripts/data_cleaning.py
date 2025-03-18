import pandas as pd
import sqlite3
import os

# Correct file path
file_path = r"C:\Users\Hp\Documents\customer_behavior_analysis\data\shopping_trends.csv"

def run():
    # Load the dataset
    df = pd.read_csv(file_path)

    # Display the first 5 rows
    print(df.head())

    # Display data types of each column
    print("Column Data Types:\n", df.dtypes)

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Check for missing values
    missing_values = df.isnull().sum()
    print("Missing Values:\n", missing_values)

    # Check for duplicates
    duplicate_count = df.duplicated().sum()
    print(f"Duplicate Rows: {duplicate_count}")

    # Define save paths (absolute paths)
    save_folder = r"C:\Users\Hp\Documents\customer_behavior_analysis\data"
    csv_file_path = rf"{save_folder}\shopping_trends_cleaned.csv"
    excel_file_path = rf"{save_folder}\shopping_trends_cleaned.xlsx"
    db_file_path = rf"{save_folder}\shopping_trends.db"

    # Ensure the directory exists before saving
    os.makedirs(save_folder, exist_ok=True)

    # Save as CSV
    df.to_csv(csv_file_path, index=False)

    # Save as Excel
    df.to_excel(excel_file_path, index=False)

    # Save as SQLite Database
    conn = sqlite3.connect(db_file_path)
    df.to_sql("shopping_trends", conn, if_exists="replace", index=False)
    conn.close()

    print("✅ Data successfully saved as CSV, Excel, and SQLite Database.")

# Run the script when executed
if __name__ == "__main__":
    run()
