import pandas as pd
import numpy as np

# File path for cleaned data
FILE_PATH = r"C:\Users\Hp\Documents\customer_behavior_analysis\data\shopping_trends_cleaned.csv"

def load_data(file_path):
    """Load the cleaned dataset from a CSV file."""
    return pd.read_csv(file_path)

def basic_info(df):
    """Display basic dataset information."""
    print("\n🔹 Dataset Info:")
    print(df.info())

def check_missing_values(df):
    """Check for missing values."""
    missing_values = df.isnull().sum()
    print("\n🔹 Missing Values:\n", missing_values[missing_values > 0])

def check_duplicates(df):
    """Check for duplicate rows."""
    duplicate_count = df.duplicated().sum()
    print(f"\n🔹 Duplicate Rows: {duplicate_count}")

def summary_statistics(df):
    """Display summary statistics for numerical and categorical columns."""
    print("\n🔹 Summary Statistics (Numerical):\n", df.describe())
    print("\n🔹 Summary Statistics (Categorical):\n", df.describe(include='object'))

def skewness_kurtosis(df):
    """Check skewness & kurtosis for numerical columns."""
    num_cols = df.select_dtypes(include=['number']).columns
    skewness = df[num_cols].skew()
    kurtosis = df[num_cols].kurtosis()
    
    print("\n🔹 Skewness:\n", skewness)
    print("\n🔹 Kurtosis:\n", kurtosis)

def correlation_matrix(df):
    """Compute correlation matrix for numerical columns."""
    print("\n🔹 Correlation Matrix:\n", df.corr())

def detect_outliers(df):
    """Detect outliers using IQR method for numerical columns."""
    num_cols = df.select_dtypes(include=['number']).columns
    outlier_summary = {}
    
    for col in num_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = df[(df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))]
        
        outlier_summary[col] = len(outliers)

    print("\n🔹 Outlier Counts (IQR Method):\n", outlier_summary)

def check_constant_columns(df):
    """Identify columns that have a single unique value."""
    constant_cols = [col for col in df.columns if df[col].nunique() == 1]
    print("\n🔹 Constant Columns (Only One Unique Value):\n", constant_cols)

def check_cardinality(df):
    """Check for high-cardinality categorical columns."""
    cat_cols = df.select_dtypes(include=['object']).columns
    cardinality = {col: df[col].nunique() for col in cat_cols}
    print("\n🔹 Categorical Column Cardinality:\n", cardinality)

def mode_unique_values(df):
    """Check the most frequent (mode) and unique values for each column."""
    print("\n🔹 Mode & Unique Values Count:")
    for col in df.columns:
        print(f"{col}: Mode = {df[col].mode()[0]}, Unique Values = {df[col].nunique()}")

def categorical_value_distribution(df):
    """Show the distribution of categorical values."""
    cat_cols = df.select_dtypes(include=['object']).columns
    print("\n🔹 Categorical Value Distributions:")
    for col in cat_cols:
        print(f"\n🔸 {col}:\n", df[col].value_counts())

def zero_variance_columns(df):
    """Identify numerical columns with zero variance (no change in values)."""
    num_cols = df.select_dtypes(include=['number']).columns
    zero_variance_cols = [col for col in num_cols if df[col].var() == 0]
    print("\n🔹 Zero Variance Columns:\n", zero_variance_cols)

def check_negative_values(df):
    """Identify negative values in numeric columns that should always be positive (e.g., price)."""
    num_cols = df.select_dtypes(include=['number']).columns
    negative_values = {col: df[df[col] < 0][col].count() for col in num_cols if (df[col] < 0).any()}
    print("\n🔹 Negative Value Counts (Possible Anomalies):\n", negative_values)

def detect_possible_typos(df):
    """Detect possible typos in categorical columns (case inconsistencies, extra spaces)."""
    cat_cols = df.select_dtypes(include=['object']).columns
    print("\n🔹 Possible Typo Detection:")
    for col in cat_cols:
        unique_values = df[col].unique()
        if any(val != val.strip() or val.lower() != val for val in unique_values):
            print(f"⚠️ {col} may contain typos or inconsistent formatting: {unique_values}")

def run():
    """Run EDA process."""
    df = load_data(FILE_PATH)
    
    basic_info(df)
    check_missing_values(df)
    check_duplicates(df)
    summary_statistics(df)
    skewness_kurtosis(df)
    correlation_matrix(df)
    detect_outliers(df)
    check_constant_columns(df)
    check_cardinality(df)
    mode_unique_values(df)
    categorical_value_distribution(df)
    zero_variance_columns(df)
    check_negative_values(df)
    detect_possible_typos(df)

    print("\n✅ EDA Completed!")

# Run the script
if __name__ == "__main__":
    run()
