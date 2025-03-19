import pandas as pd
import numpy as np
import os

# Constants
FILE_PATH = r"C:\Users\Hp\Documents\customer_behavior_analysis\data\shopping_trends_cleaned.csv"

# Load dataset
def load_data(file_path):
    """Load the cleaned dataset from a CSV file."""
    return pd.read_csv(file_path)

# Display basic info
def display_info(df):
    """Display dataset info including shape, columns, and first 5 rows."""
    print(f"\nDataset Shape: {df.shape}")
    print(f"\nColumns: {list(df.columns)}")
    print("\nFirst 5 Rows:\n", df.head())

# Check for missing values
def check_missing_values(df):
    """Check and display missing values in the dataset."""
    missing_values = df.isnull().sum()
    print("\n🔹 Missing Values:\n", missing_values[missing_values > 0])

# Check for duplicates
def check_duplicates(df):
    """Check for duplicate rows in the dataset."""
    duplicate_count = df.duplicated().sum()
    print(f"\n🔹 Duplicate Rows: {duplicate_count}")

# Display summary statistics
def summary_statistics(df):
    """Display summary statistics for numerical columns."""
    print("\n🔹 Summary Statistics (Numerical Columns):\n", df.describe())

# Unique value counts for categorical columns
def categorical_summary(df):
    """Display unique value counts for categorical columns."""
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        print(f"\n🔹 Unique values in '{col}':\n", df[col].value_counts())

# Correlation Matrix
def correlation_matrix(df):
    """Compute correlation matrix for numerical columns."""
    num_df = df.select_dtypes(include=['number'])  # Select only numerical columns
    if num_df.shape[1] > 1:  # Ensure at least 2 numerical columns exist
        print("\n🔹 Correlation Matrix:\n", num_df.corr())
    else:
        print("\n⚠️ Not enough numerical columns for correlation analysis.")

# Data type validation
def validate_data_types(df):
    """Check if the data types are appropriate for analysis."""
    print("\n🔹 Column Data Types:\n", df.dtypes)

# Run function
def run():
    """Main function to execute EDA steps."""
    df = load_data(FILE_PATH)
    display_info(df)
    check_missing_values(df)
    check_duplicates(df)
    summary_statistics(df)
    categorical_summary(df)
    correlation_matrix(df)
    validate_data_types(df)

# Execute the script
if __name__ == "__main__":
    run()