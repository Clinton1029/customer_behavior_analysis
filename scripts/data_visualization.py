import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set Seaborn theme for modern styling
sns.set_theme(style="darkgrid")

# File path to the cleaned dataset
DATA_PATH = r"C:\Users\Hp\Documents\customer_behavior_analysis\data\shopping_trends_cleaned.csv"

# Ensure the file exists before loading
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"❌ The cleaned dataset was not found at: {DATA_PATH}")

# Load the cleaned dataset
df = pd.read_csv(DATA_PATH)

# Convert purchase_date to datetime if available
if "purchase_date" in df.columns:
    df["purchase_date"] = pd.to_datetime(df["purchase_date"], errors="coerce")

# ---------------------- MODERN VISUALIZATION FUNCTIONS ---------------------- #

def plot_category_distribution(column_name, title):
    """Plots the distribution of a categorical column using a modern bar chart."""
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=df[column_name].value_counts().index, 
        y=df[column_name].value_counts().values, 
        palette="coolwarm", edgecolor="black"
    )
    plt.title(title, fontsize=18, fontweight="bold", color="white")
    plt.xlabel(column_name.replace("_", " ").title(), fontsize=14, fontweight="bold", color="white")
    plt.ylabel("Count", fontsize=14, color="white")
    plt.xticks(rotation=30, fontsize=12, color="white")
    plt.yticks(fontsize=12, color="white")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.gca().set_facecolor("#222222")  # Dark background
    plt.show()

def plot_histogram(column_name, title, bins=25):
    """Plots a histogram for a numerical column with professional styling."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column_name], bins=bins, kde=True, color="deepskyblue", edgecolor="black", alpha=0.8)
    plt.title(title, fontsize=18, fontweight="bold", color="white")
    plt.xlabel(column_name.replace("_", " ").title(), fontsize=14, fontweight="bold", color="white")
    plt.ylabel("Frequency", fontsize=14, color="white")
    plt.xticks(fontsize=12, color="white")
    plt.yticks(fontsize=12, color="white")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.gca().set_facecolor("#222222")  # Dark background
    plt.show()

def plot_scatter(x_column, y_column, title):
    """Creates a modern scatter plot for two numerical columns."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df[x_column], y=df[y_column], alpha=0.7, color="limegreen", edgecolor="white")
    plt.title(title, fontsize=18, fontweight="bold", color="white")
    plt.xlabel(x_column.replace("_", " ").title(), fontsize=14, fontweight="bold", color="white")
    plt.ylabel(y_column.replace("_", " ").title(), fontsize=14, color="white")
    plt.xticks(fontsize=12, color="white")
    plt.yticks(fontsize=12, color="white")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.gca().set_facecolor("#222222")  # Dark background
    plt.show()

def plot_line_chart(x_column, y_column, title):
    """Creates a sleek, professional line chart for trend analysis."""
    if df[x_column].isnull().all():
        print(f"⚠️ Skipping line chart: {x_column} contains only null values.")
        return

    plt.figure(figsize=(12, 6))
    df_sorted = df.sort_values(by=x_column)
    sns.lineplot(x=df_sorted[x_column], y=df_sorted[y_column], color="gold", marker="o", linewidth=2.5)
    plt.title(title, fontsize=18, fontweight="bold", color="white")
    plt.xlabel(x_column.replace("_", " ").title(), fontsize=14, fontweight="bold", color="white")
    plt.ylabel(y_column.replace("_", " ").title(), fontsize=14, color="white")
    plt.xticks(rotation=45, fontsize=12, color="white")
    plt.yticks(fontsize=12, color="white")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.gca().set_facecolor("#222222")  # Dark background
    plt.show()

# ---------------------- RUN FUNCTION ---------------------- #

def run():
    """Runs the visualization process with modern, professional styling."""
    print("📊 Generating professional visualizations...\n")

    # 1. Customer Gender Distribution
    plot_category_distribution("gender", "Customer Gender Breakdown")

    # 2. Payment Methods Usage
    plot_category_distribution("payment_method", "Most Preferred Payment Methods")

    # 3. Purchase Amount Distribution
    plot_histogram("purchase_amount_(usd)", "Distribution of Purchase Amounts (USD)")

    # 4. Age vs. Purchase Amount
    plot_scatter("age", "purchase_amount_(usd)", "Impact of Age on Purchase Amount")

    # 5. Previous Purchases vs. Purchase Amount
    plot_scatter("previous_purchases", "purchase_amount_(usd)", "Effect of Past Purchases on Spending")

    # 6. Purchase Trends Over Time
    if "purchase_date" in df.columns:
        plot_line_chart("purchase_date", "purchase_amount_(usd)", "Purchase Amount Trend Over Time")

    print("✅ Modern visualizations generated successfully!")

# Run the script when executed
if __name__ == "__main__":
    run()
