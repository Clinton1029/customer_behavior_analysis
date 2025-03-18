import pandas as pd

# Correct file path
file_path = r"C:\Users\Hp\Documents\customer_behavior_analysis\data\shopping_trends.csv"


# Load the dataset
df = pd.read_csv(file_path)

# Display the first 5 rows
print(df.head())
