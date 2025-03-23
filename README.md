# 📊 Customer Behavior Analysis

## 🌟 Overview
This project analyzes customer shopping behaviors using a dataset containing demographic, transaction, and behavioral data. The goal is to gain insights into customer spending habits, preferences, and trends.

## 🛠 Tools & Technologies Used
- 🐍 **Python** (Data Processing & Analysis)
- 🗂 **Pandas** (Data Cleaning & Manipulation)
- 🔢 **NumPy** (Numerical Computations)
- 📊 **Matplotlib** (Data Visualization)
- 🎨 **Seaborn** (Advanced Visualizations)
- 🌍 **GitHub** (Version Control & Documentation)

## 🧼 Data Cleaning & Preprocessing
- 📝 **Handling Missing Values:** Removed or imputed missing data. *(Tools: Pandas, NumPy)*
- 📏 **Data Formatting:** Standardized date formats, numerical values, and categorical labels. *(Tools: Pandas, NumPy)*
- 🚨 **Outlier Detection:** Identified and removed extreme values affecting analysis. *(Tools: Pandas, NumPy, Seaborn)*
- 🏗 **Feature Engineering:** Created new features for better insights, such as customer lifetime value. *(Tools: Pandas, NumPy)*

## 📈 Key Insights from Visualizations
### 📌 Trend of Purchase Amounts Based on Previous Purchases
![Trend of Purchase Amounts](https://github.com/Clinton1029/customer_behavior_analysis/blob/main/Figure_17.png)
- The purchase amount distribution remains relatively stable across different purchase histories.

- There is no strong upward or downward trend, implying that past purchases do not heavily influence future spending.

- Customers with fewer previous purchases still exhibit high spending, showing that new customers can also be high-value.

- Some fluctuations exist, suggesting that external factors like promotions or seasonality may impact spending.

- There are outliers with exceptionally high purchases despite having fewer prior transactions.
### 💰 Previous Purchases vs. Purchase Amount (USD)
![Previous Purchases vs. Amount](https://github.com/Clinton1029/customer_behavior_analysis/blob/main/Figure_15.png)
- The scatter plot shows a wide variance in spending regardless of previous purchase history.

- Customers with repeated purchases do not necessarily spend more than first-time buyers.

- Some individuals with high previous purchases maintain steady spending, indicating consistent shopping behavior.

- High purchase amounts occur at both low and high previous purchase counts, reflecting diverse customer profiles.

- No clear linear correlation suggests that repeat customers do not automatically increase their spending over time.
### 👵🧑 Age vs. Purchase Amount (USD)
![Age vs. Purchase Amount](https://github.com/Clinton1029/customer_behavior_analysis/blob/main/Figure_14.png)
- Purchase amounts are fairly consistent across different age groups.
- No strong correlation between age and spending behavior. *(Tools: Matplotlib, Seaborn)*

### 📊 Distribution of Purchase Amounts (USD)
![Purchase Amount Distribution](https://github.com/Clinton1029/customer_behavior_analysis/blob/main/Figure_13.png)
- The histogram shows a relatively uniform distribution of purchase amounts, with higher frequencies near the upper limit.
- Customers tend to make purchases in all price ranges, with some preference toward higher amounts. *(Tools: Matplotlib, Seaborn)*

### 💳 Payment Methods Used by Customers
![Payment Methods](https://github.com/Clinton1029/customer_behavior_analysis/blob/main/Figure_11.png)
- Credit cards are the most commonly used payment method.
- Other methods, such as Venmo, PayPal, and Debit Card, are also widely used but slightly less frequent. *(Tools: Matplotlib, Seaborn)*

### 👥 Customer Gender Distribution
![Gender Distribution](https://github.com/Clinton1029/customer_behavior_analysis/blob/main/Figure_12.png)
- Male customers outnumber female customers significantly.
- This imbalance may suggest a targeted audience or differences in shopping preferences between genders. *(Tools: Matplotlib, Seaborn)*

## 🔮 Next Steps
- 🔍 Conduct customer segmentation using clustering techniques.
- 📈 Implement predictive modeling to forecast customer behavior.
- 📊 Improve data visualization with interactive dashboards.

## 🚀 How to Run the Project
1. 📥 Clone the repository.
2. ⚙️ Install the required dependencies.
3. 🏃 Run the data processing scripts.
4. 📊 Generate visualizations to explore insights.

---


