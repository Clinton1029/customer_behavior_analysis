import sys
import os

# Ensure the scripts directory is in Python's module search path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.append(SCRIPT_DIR)

# Import necessary modules
try:
   
    import eda
    import insights
    import data_visualization
except ModuleNotFoundError as e:
    print(f"❌ Module import error: {e}")
    print("🔹 Ensure all scripts are in the 'scripts' directory and named correctly.")
    sys.exit(1)

def run():
    """Runs the full customer behavior analysis pipeline."""
    print("\n🚀 Running Customer Behavior Analysis Pipeline...\n")

    
    # Step 2: Exploratory Data Analysis (EDA)
    print("\n🔹 Step 2: Performing Exploratory Data Analysis (EDA)")
    eda.run()

    # Step 3: Generating Insights
    print("\n🔹 Step 3: Extracting Insights")
    insights.run()

    # Step 4: Creating Visualizations
    print("\n🔹 Step 4: Generating Visualizations")
    data_visualization.run()

    print("\n✅ Customer Behavior Analysis Pipeline Completed Successfully!")

if __name__ == "__main__":
    run()
