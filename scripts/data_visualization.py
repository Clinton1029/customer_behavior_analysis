import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------------------- CONSTANTS ---------------------- #
DATA_PATH = r"C:\Users\Hp\Documents\customer_behavior_analysis\data\shopping_trends_cleaned.csv"

# ---------------------- DATA LOADING ---------------------- #
def load_data(file_path):
    """Load the cleaned dataset and ensure the file exists."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ The cleaned dataset was not found at: {file_path}")
    return pd.read_csv(file_path)

# Load the dataset
df = load_data(DATA_PATH)

# ---------------------- VISUALIZATION FUNCTIONS ---------------------- #
def plot_category_distribution(column_name, title):
    """Plots the distribution of a categorical column with professional formatting."""
    plt.figure(figsize=(10, 5))
    df[column_name].value_counts().plot(kind="bar", color="royalblue", edgecolor="black")
    plt.title(title, fontsize=16, fontweight="bold", color="darkblue")
    plt.xlabel(column_name.replace("_", " ").title(), fontsize=12, fontweight="bold")
    plt.ylabel("Count", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

def plot_histogram(column_name, title, bins=20):
    """Plots a histogram for a numerical column with professional styling."""
    plt.figure(figsize=(10, 5))
    plt.hist(df[column_name], bins=bins, color="darkorange", edgecolor="black", alpha=0.7)
    plt.title(title, fontsize=16, fontweight="bold", color="darkblue")
    plt.xlabel(column_name.replace("_", " ").title(), fontsize=12, fontweight="bold")
    plt.ylabel("Frequency", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

def plot_scatter(x_column, y_column, title):
    """Creates a scatter plot for two numerical columns with professional formatting."""
    plt.figure(figsize=(10, 5))
    plt.scatter(df[x_column], df[y_column], color="seagreen", alpha=0.5)
    plt.title(title, fontsize=16, fontweight="bold", color="darkblue")
    plt.xlabel(x_column.replace("_", " ").title(), fontsize=12, fontweight="bold")
    plt.ylabel(y_column.replace("_", " ").title(), fontsize=12, fontweight="bold")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.show()

def plot_line_chart(x_column, y_column, title):
    """Creates a line chart to visualize trends over time with professional styling."""
    if x_column not in df.columns or y_column not in df.columns:
        print(f"⚠️ Skipping line chart: Columns {x_column} or {y_column} not found.")
        return

    plt.figure(figsize=(12, 5))
    df_sorted = df.sort_values(by=x_column)  # Ensure data is sorted
    plt.plot(df_sorted[x_column], df_sorted[y_column], color="blue", marker="o", linestyle="-", alpha=0.7)
    plt.title(title, fontsize=16, fontweight="bold", color="darkblue")
    plt.xlabel(x_column.replace("_", " ").title(), fontsize=12, fontweight="bold")
    plt.ylabel(y_column.replace("_", " ").title(), fontsize=12, fontweight="bold")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.show()

# ---------------------- RUN FUNCTION ---------------------- #
def run():
    """Runs the visualization process with professional chart titles."""
    print("📊 Generating visualizations...\n")
    
    # 1. Distribution of Gender
    plot_category_distribution("gender", "Customer Gender Distribution")

    # 2. Distribution of Payment Methods
    plot_category_distribution("payment_method", "Payment Methods Used by Customers")

    # 3. Purchase Amount Distribution
    plot_histogram("purchase_amount_(usd)", "Distribution of Purchase Amounts (USD)")

    # 4. Relationship between Age and Purchase Amount
    plot_scatter("age", "purchase_amount_(usd)", "Age vs. Purchase Amount (USD)")

    # 5. Relationship between Previous Purchases and Purchase Amount
    plot_scatter("previous_purchases", "purchase_amount_(usd)", "Previous Purchases vs. Purchase Amount (USD)")

    # 6. Purchase Amount Trend Based on Previous Purchases (Line Chart)
    plot_line_chart("previous_purchases", "purchase_amount_(usd)", "Trend of Purchase Amounts Based on Previous Purchases")

    print("✅ Visualizations generated successfully!")

# ---------------------- SCRIPT EXECUTION ---------------------- #
if __name__ == "__main__":
    run()