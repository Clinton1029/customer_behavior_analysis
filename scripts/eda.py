import pandas as pd
import numpy as np
import os

# Constants
FILE_PATH = r"C:\Users\Hp\Documents\customer_behavior_analysis\data\shopping_trends_cleaned.csv"

# Utility Functions
def load_data(file_path):
    """Load the cleaned dataset from a CSV file."""
    return pd.read_csv(file_path)

def display_info(df):
    """Display dataset info including shape, columns, and first 5 rows."""
    print(f"\n🔹 Dataset Shape: {df.shape}")
    print(f"\n🔹 Columns: {list(df.columns)}")
    print("\n🔹 First 5 Rows:\n", df.head())

def check_missing_values(df):
    """Check and display missing values in the dataset."""
    missing_values = df.isnull().sum()
    if missing_values.any():
        print("\n🔹 Missing Values:\n", missing_values[missing_values > 0])
    else:
        print("\n✅ No missing values found.")

def check_duplicates(df):
    """Check for duplicate rows in the dataset."""
    duplicate_count = df.duplicated().sum()
    print(f"\n🔹 Duplicate Rows: {duplicate_count}")

def summary_statistics(df):
    """Display summary statistics for numerical columns."""
    print("\n🔹 Summary Statistics (Numerical Columns):\n", df.describe())

def categorical_summary(df):
    """Display unique value counts for categorical columns."""
    cat_cols = df.select_dtypes(include=['object']).columns
    if len(cat_cols) > 0:
        for col in cat_cols:
            print(f"\n🔹 Unique values in '{col}':\n", df[col].value_counts())
    else:
        print("\n✅ No categorical columns found.")

def correlation_matrix(df):
    """Compute and display the correlation matrix for numerical columns."""
    num_df = df.select_dtypes(include=['number'])  # Select only numerical columns
    if num_df.shape[1] > 1:  # Ensure at least 2 numerical columns exist
        print("\n🔹 Correlation Matrix:\n", num_df.corr())
    else:
        print("\n⚠️ Not enough numerical columns for correlation analysis.")

def validate_data_types(df):
    """Check if the data types are appropriate for analysis."""
    print("\n🔹 Column Data Types:\n", df.dtypes)

# Main Function
def run():
    """Main function to execute EDA steps."""
    print("\n🔍 Starting Exploratory Data Analysis (EDA)...")
    df = load_data(FILE_PATH)
    display_info(df)
    check_missing_values(df)
    check_duplicates(df)
    summary_statistics(df)
    categorical_summary(df)
    correlation_matrix(df)
    validate_data_types(df)
    print("\n✅ EDA Completed Successfully!")

# Execute the script
if __name__ == "__main__":
    run()