# Exploratory Data Analysis: E-Commerce Sales Drivers

**Objective:** To diagnose the underlying drivers of high-value orders and evaluate the effectiveness of current promotional strategies.

**Tech Stack:** Python (Pandas, Matplotlib, Seaborn)

## 1. The Core Business Problem
The business required a forensic analysis of recent sales data to answer two critical questions:
* Who are our VIP customers, and what drives their high-value purchases?
* Are our current promotional discount codes actively incentivizing larger cart sizes?

## 2. Methodology
To ensure data integrity, I processed the raw evidence through a strict analytical pipeline:
* **Data Cleansing:** Sanitized the dataset by standardizing invalid date formats and handling over 300 missing values in the promotional code category.
* **Locating the Center:** Applied the Five-Number Summary to establish baseline revenue metrics and identify a right-skewed distribution.
* **Signal Detection:** Deployed the Interquartile Range (IQR) method to mathematically isolate extreme VIP outlier orders from standard organic traffic.

## 3. Key Findings & Insights
* **Social Media Dominance:** Facebook referrals generate the highest average total spend ($1,098), outperforming both Instagram and Google.
* **The VIP Profile:** The top 1% of highest-spending orders are driven almost entirely by maximum-quantity bulk purchases of high-ticket electronics.
* **Coupon Inefficiency:** Current promotional codes (`WINTER15`, `SAVE10`) are failing to increase cart sizes. Customers using no coupon actually averaged the highest cart size (5.56 items).

## 4. Business Impact & Recommendations
Based on the verified insights, I recommend the following strategic pivots:
1. **Target B2B Bulk Buyers:** Pivot ad spend toward B2B clients or office managers upgrading their tech, as they drive our maximum revenue.
2. **Reallocate Marketing Budget:** Shift marketing efforts away from lower-performing channels and double down on Facebook.
3. **Restructure Discounts:** Phase out flat-rate coupons and implement threshold-based incentives (example:, "15% off orders of 6 or more items") to actively force an increase in average cart sizes.