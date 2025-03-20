import sys
import os

# Add the scripts directory to Python's module search path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(SCRIPT_DIR)

# Import the project modules
import data_cleaning
import eda
import insights
import visualization

def run():
    """Runs the full customer behavior analysis pipeline."""
    print("\n🚀 Running Customer Behavior Analysis Pipeline...\n")

    print("🔹 Step 1: Data Cleaning")
    data_cleaning.run()

    print("\n🔹 Step 2: Exploratory Data Analysis (EDA)")
    eda.run()

    print("\n🔹 Step 3: Generating Insights")
    insights.run()

    print("\n🔹 Step 4: Creating Visualizations")
    visualization.run()

    print("\n✅ Pipeline Completed Successfully!")

if __name__ == "__main__":
    run()
