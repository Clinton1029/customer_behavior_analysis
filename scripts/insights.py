import pandas as pd
import os

# Constants
DATA_PATH = r"C:\Users\Hp\Documents\customer_behavior_analysis\data\shopping_trends_cleaned.csv"

def load_data(file_path):
    """Load the cleaned dataset."""
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        raise FileNotFoundError(f"⚠️ The file '{file_path}' does not exist.")

def top_purchased_categories(df, top_n=5):
    """Find the top N most purchased categories."""
    return df["category"].value_counts().head(top_n)

def high_spending_customers(df, top_n=5):
    """Identify the top N customers who spent the most."""
    return df.groupby("customer_id")["purchase_amount_(usd)"].sum().nlargest(top_n)

def avg_spending_by_gender(df):
    """Calculate average spending per gender."""
    return df.groupby("gender")["purchase_amount_(usd)"].mean()

def popular_payment_methods(df):
    """Find the most frequently used payment methods."""
    return df["payment_method"].value_counts()

def frequent_buyers(df, min_purchases=5):
    """Identify customers who made at least `min_purchases` purchases."""
    return df["customer_id"].value_counts()[df["customer_id"].value_counts() >= min_purchases]

def subscription_status_analysis(df):
    """Compare spending between subscribed and non-subscribed customers."""
    return df.groupby("subscription_status")["purchase_amount_(usd)"].mean()

def seasonality_analysis(df):
    """Find the most common season for shopping trends."""
    return df["season"].value_counts()

def discount_usage(df):
    """Check the proportion of purchases that had a discount applied."""
    return df["discount_applied"].value_counts(normalize=True) * 100

def generate_insights(df):
    """Generate key insights from the data."""
    print("\n🔹 **Top Purchased Categories:**")
    print(top_purchased_categories(df))

    print("\n🔹 **High Spending Customers:**")
    print(high_spending_customers(df))

    print("\n🔹 **Average Spending by Gender:**")
    print(avg_spending_by_gender(df))

    print("\n🔹 **Most Popular Payment Methods:**")
    print(popular_payment_methods(df))

    print("\n🔹 **Frequent Buyers (5+ purchases):**")
    print(frequent_buyers(df))

    print("\n🔹 **Spending by Subscription Status:**")
    print(subscription_status_analysis(df))

    print("\n🔹 **Seasonal Shopping Trends:**")
    print(seasonality_analysis(df))

    print("\n🔹 **Discount Usage in Purchases (%):**")
    print(discount_usage(df))

    print("\n✅ **Insights Generation Completed!**")

def run():
    """Run the insights generation process."""
    df = load_data(DATA_PATH)
    generate_insights(df)

if __name__ == "__main__":
    run()
