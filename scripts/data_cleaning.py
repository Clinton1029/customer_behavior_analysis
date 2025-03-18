import pandas as pd

# Correct file path
file_path = r"C:\Users\Hp\Documents\customer_behavior_analysis\data\shopping_trends.csv"


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



