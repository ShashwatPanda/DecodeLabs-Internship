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

# df.to_excel("Cleaned_dataset.xlsx",index=False)
# print("Done successfully!")

# ------------------------------------------
# PHASE 2: EXPLORATORY DATA ANALYSIS (EDA) & STATISTICS
# ------------------------------------------

print("\n--- Starting Phase 2: EDA & Statistics ---")

Price_Analysis = df["TotalPrice"].describe()
Median = df["TotalPrice"].median()
print(Price_Analysis)
print(Median)

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

coupon_impact = df.groupby('CouponCode')[['ItemsInCart', 'TotalPrice']].mean()
coupon_impact = coupon_impact.sort_values(by='TotalPrice', ascending=False)

print("\nAverage Spend and Cart Size by Coupon Code:")
print(coupon_impact)

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