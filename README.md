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
- Customers across all age groups have similar spending ranges.

- No significant peak or dip, meaning age is not a strong predictor of purchase amount.

- Young adults and middle-aged customers show the most variation in spending behavior.

- Older customers (above 50) still contribute significantly to high-value transactions.

- The spread suggests that marketing efforts should be tailored based on factors beyond just age.
### 📊 Distribution of Purchase Amounts (USD)
![Purchase Amount Distribution](https://github.com/Clinton1029/customer_behavior_analysis/blob/main/Figure_13.png)
- Purchase amounts are spread across all ranges, but higher frequencies appear at certain spending levels.

- There are peaks at specific intervals, suggesting pricing strategies or common purchase bundles.

- Some customers make small purchases consistently, while others make occasional high-value purchases.

- The right-skewed distribution indicates that while most customers spend within a common range, a few outliers contribute to significantly high revenue.

- High-value purchases, though less frequent, are essential for revenue growth.
### 💳 Payment Methods Used by Customers
![Payment Methods](https://github.com/Clinton1029/customer_behavior_analysis/blob/main/Figure_11.png)
- Credit cards dominate, suggesting customer preference for cashless payments.

- PayPal and Venmo are widely used, showing that digital wallets are growing in popularity.

- Debit card usage is slightly lower, possibly due to credit rewards or installment options.

- The presence of multiple payment methods highlights the importance of offering diverse payment solutions.

- Alternative payment methods (e.g., Buy Now Pay Later) could further increase sales.
### 👥 Customer Gender Distribution
![Gender Distribution](https://github.com/Clinton1029/customer_behavior_analysis/blob/main/Figure_12.png)
- Male customers outnumber female customers significantly.

- This could indicate targeted marketing efforts favoring male shoppers.

- The imbalance suggests potential growth opportunities in female-oriented products or services.

- Gender-specific shopping behaviors may impact promotional strategies.

- Further analysis is needed to understand whether male customers contribute to higher revenue or just higher numbers.
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


