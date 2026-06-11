import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------
# PHASE 1: DATA CLEANING & FORENSICS
# ------------------------------------------

print("--- Starting Phase 1: Data Cleaning & Forensics ---")

df = pd.read_excel('Dataset for Data Analytics.xlsx')

print(df.info())

print(df.isnull().sum())

df['CouponCode'] = df['CouponCode'].fillna("None")
print(df['CouponCode'].value_counts())

df['Date'] = df['Date'].dt.date

df = df.dropna(subset=['Date'])

print(f"Remaining valid records: {len(df)}")

print(f"Duplicates found: {df.duplicated().sum()}")

df = df.drop_duplicates()

print(df.head())

# ------------------------------------------
# PHASE 2: EXPLORATORY DATA ANALYSIS (EDA) & STATISTICS
# ------------------------------------------

print("\n--- Starting Phase 2: EDA & Statistics ---")

Price_Analysis = df["TotalPrice"].describe()
Median = df["TotalPrice"].median()
print(Price_Analysis)
print(Median)

print("\n--- Shape of the Evidence (Distribution Skewness) ---")
print(f"TotalPrice Skewness: {df['TotalPrice'].skew():.2f}")
print(f"Quantity Skewness: {df['Quantity'].skew():.2f}")
print(f"ItemsInCart Skewness: {df['ItemsInCart'].skew():.2f}")

print("\n--- Volumetric Metrics Summary ---")
print(df[['Quantity', 'ItemsInCart', 'UnitPrice']].describe())

print("\n--- Core Revenue & Volumetric Totals ---")
print(f"Total Gross Sales Revenue: ${df['TotalPrice'].sum():,.2f}")
print(f"Total Quantity of Products Sold: {df['Quantity'].sum():,}")
print(f"Total Transactions Logged: {len(df):,}")

print("\n--- Customer Basket Dynamics ---")
print(f"Average Items in Cart per Order: {df['ItemsInCart'].mean():.1f}")
print(f"Average Units Purchased per Product Line: {df['Quantity'].mean():.1f}")
print(f"Average Price per Individual Unit: ${df['UnitPrice'].mean():,.2f}")

# ------------------------------------------
# PHASE 3: CORRELATION & OUTLIER DETECTION
# ------------------------------------------

print("\n--- Starting Phase 3: Outliers & Trends ---")

Q1 = df['TotalPrice'].quantile(0.25)
Q3 = df['TotalPrice'].quantile(0.75)

IQR = Q3 - Q1

upper_cap = Q3 + (1.5 * IQR)
print(f"Any order above ${upper_cap:.2f} is an Outlier (VIP Order)")

outliers = df[df['TotalPrice'] > upper_cap]

print(f"Total Number of VIP Outlier Orders Found: {len(outliers)}")

print("\nCoupons used by VIPs:")
print(outliers['CouponCode'].value_counts())

vip_revenue_share = (outliers['TotalPrice'].sum() / df['TotalPrice'].sum()) * 100
print(f"VIP Outliers Revenue Contribution: {vip_revenue_share:.2f}% of total gross sales")

print("\n--- Correlation Analysis ---")

numerical_df = df[['Quantity', 'UnitPrice', 'ItemsInCart', 'TotalPrice']]

correlation_matrix = numerical_df.corr(method='pearson')
print(correlation_matrix)

items_price_corr = df['ItemsInCart'].corr(df['TotalPrice'])
print(f"\nCorrelation between Items in Cart and Total Price: {items_price_corr:.2f}")

print("\n---Investigating hidden details---")

referral_impact = df.groupby('ReferralSource')[['ItemsInCart', 'TotalPrice']].mean()

referral_impact = referral_impact.sort_values(by='TotalPrice',ascending=False)

print(referral_impact)

print("\n--- Total Revenue and Order Volumetrics by Referral Source ---")
referral_totals = df.groupby('ReferralSource')['TotalPrice'].agg(['sum', 'count']).sort_values(by='sum', ascending=False)
print(referral_totals)

coupon_impact = df.groupby('CouponCode')[['ItemsInCart', 'TotalPrice']].mean()
coupon_impact = coupon_impact.sort_values(by='TotalPrice', ascending=False)

print("\nAverage Spend and Cart Size by Coupon Code:")
print(coupon_impact)

print("\n--- Gross Revenue Driven by Coupon Code Campaign ---")
coupon_totals = df.groupby('CouponCode')['TotalPrice'].agg(['sum', 'count']).sort_values(by='sum', ascending=False)
print(coupon_totals)

print("\n--- Order Metrics Breakdown by Unit Price Tiers ---")
df['PriceTier'] = pd.qcut(df['UnitPrice'], q=3, labels=['Low Value Line', 'Mid Value Line', 'High Value Line'])
tier_analysis = df.groupby('PriceTier')[['Quantity', 'TotalPrice']].agg(['mean', 'sum'])
print(tier_analysis)

print("\n--- Referral Traffic Segmentation Cross-Tabulation (Standard vs VIP %) ---")
df['OrderSegment'] = ['VIP Outlier' if x > upper_cap else 'Standard Order' for x in df['TotalPrice']]
segment_cross = pd.crosstab(df['ReferralSource'], df['OrderSegment'], normalize='index') * 100
print(segment_cross.round(2))

# ------------------------------------------
# PHASE 4: VISUALIZING THE EVIDENCE
# ------------------------------------------

print("\n---Starting Phase 4: Visualizing the Evidence---")

plot_data = referral_impact.reset_index()

sns.set_theme(style="white")

fig, ax = plt.subplots(figsize=(10, 6))

colors = ['#0088ff' if source == 'Facebook' else '#d3d3d3' for source in plot_data['ReferralSource']]

sns.barplot(
    x='TotalPrice', 
    y='ReferralSource', 
    data=plot_data, 
    palette=colors, 
    ax=ax
)

sns.despine(left=True, bottom=True)
ax.set_ylabel('') 
ax.set_xlabel('') 
ax.set_xticks([])  

for p in ax.patches:
    width = p.get_width()
    ax.annotate(f'${width:,.0f}', 
                (width + 20, p.get_y() + p.get_height() / 2), 
                ha='left', va='center', fontsize=11, fontweight='bold')

plt.title('Facebook Referrals Drive the Highest Average Spend', 
          loc='left', fontsize=16, fontweight='bold', pad=20)

plt.show()