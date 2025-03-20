import pandas as pd
import matplotlib.pyplot as plt
import os

# File path to the cleaned dataset
DATA_PATH = r"C:\Users\Hp\Documents\customer_behavior_analysis\data\shopping_trends_cleaned.csv"

# Ensure the file exists before loading
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"❌ The cleaned dataset was not found at: {DATA_PATH}")

# Load the cleaned dataset
df = pd.read_csv(DATA_PATH)

# ---------------------- VISUALIZATION FUNCTIONS ---------------------- #

def plot_category_distribution(column_name, title, xlabel, ylabel):
    """Plots the distribution of a categorical column."""
    plt.figure(figsize=(10, 5))
    df[column_name].value_counts().plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

def plot_histogram(column_name, bins=20):
    """Plots a histogram for a numerical column."""
    plt.figure(figsize=(10, 5))
    plt.hist(df[column_name], bins=bins, color="lightcoral", edgecolor="black", alpha=0.7)
    plt.title(f"Distribution of {column_name}", fontsize=14)
    plt.xlabel(column_name, fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

def plot_scatter(x_column, y_column):
    """Creates a scatter plot for two numerical columns."""
    plt.figure(figsize=(10, 5))
    plt.scatter(df[x_column], df[y_column], color="seagreen", alpha=0.5)
    plt.title(f"{x_column} vs {y_column}", fontsize=14)
    plt.xlabel(x_column, fontsize=12)
    plt.ylabel(y_column, fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.show()

# ---------------------- RUN FUNCTION ---------------------- #

def run():
    """Runs the visualization process."""
    print("📊 Generating visualizations...\n")
    
    # 1. Distribution of Gender
    plot_category_distribution("gender", "Gender Distribution", "Gender", "Count")
    
    # 2. Distribution of Payment Methods
    plot_category_distribution("payment_method", "Payment Method Distribution", "Payment Method", "Count")
    
    # 3. Purchase Amount Distribution
    plot_histogram("purchase_amount_(usd)")
    
    # 4. Relationship between Age and Purchase Amount
    plot_scatter("age", "purchase_amount_(usd)")
    
    # 5. Relationship between Previous Purchases and Purchase Amount
    plot_scatter("previous_purchases", "purchase_amount_(usd)")

    print("✅ Visualizations generated successfully!")

# Run the script when executed
if __name__ == "__main__":
    run()
