# Roadmap.sh
"""
Pharmaceutical Sales Data Analysis
This script analyzes pharmaceutical sales data to answer key business questions
about drug sales patterns, categories, and trends.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Set visualization style
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 6)

print("="*60)
print("PHARMACEUTICAL SALES DATA ANALYSIS")
print("="*60)

# Load the dataset
print("\n1. Loading data...")
df = pd.read_csv('data/salesdaily.csv')
print(f"   Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# Convert date column to datetime
df['datum'] = pd.to_datetime(df['datum'])

# Define drug category columns (ATC codes)
drug_columns = ['M01AB', 'M01AE', 'N02BA', 'N02BE', 'N05B', 'N05C', 'R03', 'R06']

print(f"   Date range: {df['datum'].min()} to {df['datum'].max()}")
print(f"   Drug categories: {len(drug_columns)}")


# QUESTION 1: Total Sales Quantities by Drug Category (ATC Code)

print("\n" + "="*60)
print("QUESTION 1: Total Sales Quantities by Drug Category")
print("="*60)

total_sales = df[drug_columns].sum().sort_values(ascending=False)

for drug, sales in total_sales.items():
    print(f"   {drug}: {sales:,.2f}")

# Visualize
plt.figure(figsize=(10, 6))
total_sales.plot(kind='bar', color='steelblue', edgecolor='black')
plt.title('Total Sales Quantities by Drug Category (ATC Code)', fontsize=16, fontweight='bold')
plt.xlabel('Drug Category (ATC Code)', fontsize=12)
plt.ylabel('Total Sales Quantity', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('output_q1_total_sales.png', dpi=300, bbox_inches='tight')
print("\n   📊 Chart saved: output_q1_total_sales.png")


# QUESTION 2: Individual Drug Brands with Highest Total Sales

print("\n" + "="*60)
print("QUESTION 2: Drug Categories Ranked by Total Sales")
print("="*60)

top_drugs = total_sales.sort_values(ascending=True)

for i, (drug, sales) in enumerate(reversed(list(top_drugs.items())), 1):
    print(f"   {i}. {drug}: {sales:,.2f}")

# Visualize
plt.figure(figsize=(10, 6))
top_drugs.plot(kind='barh', color='coral', edgecolor='black')
plt.title('Drug Categories Ranked by Total Sales', fontsize=16, fontweight='bold')
plt.xlabel('Total Sales Quantity', fontsize=12)
plt.ylabel('Drug Category (ATC Code)', fontsize=12)
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('output_q2_ranked_sales.png', dpi=300, bbox_inches='tight')
print("\n   📊 Chart saved: output_q2_ranked_sales.png")


# QUESTION 3: Top Three Drugs in Specific Months

print("\n" + "="*60)
print("QUESTION 3: Top 3 Drugs in Specific Months")
print("="*60)

def get_top_drugs_for_month(df, year, month, month_name):
    mask = (df['Year'] == year) & (df['Month'] == month)
    filtered_df = df[mask]
    monthly_sales = filtered_df[drug_columns].sum().sort_values(ascending=False)
    top_3 = monthly_sales.head(3)
    
    print(f"\n   {month_name} {year}:")
    for i, (drug, sales) in enumerate(top_3.items(), 1):
        print(f"      {i}. {drug}: {sales:,.2f}")
    
    return top_3

jan_2015 = get_top_drugs_for_month(df, 2015, 1, "January")
jul_2016 = get_top_drugs_for_month(df, 2016, 7, "July")
sep_2017 = get_top_drugs_for_month(df, 2017, 9, "September")

# Visualize comparison
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
periods = [
    (jan_2015, "January 2015", axes[0]),
    (jul_2016, "July 2016", axes[1]),
    (sep_2017, "September 2017", axes[2])
]

for data, title, ax in periods:
    data.plot(kind='bar', ax=ax, color='teal', edgecolor='black')
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel('Drug Category', fontsize=10)
    ax.set_ylabel('Sales Quantity', fontsize=10)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('output_q3_specific_months.png', dpi=300, bbox_inches='tight')
print("\n   📊 Chart saved: output_q3_specific_months.png")


# QUESTION 4: Drug Sold Most Often in 2017

print("\n" + "="*60)
print("QUESTION 4: Drug Sold Most Often in 2017")
print("="*60)

df_2017 = df[df['Year'] == 2017]

# Count non-zero sales days
sales_frequency = {}
for drug in drug_columns:
    non_zero_days = (df_2017[drug] > 0).sum()
    sales_frequency[drug] = non_zero_days

freq_series = pd.Series(sales_frequency).sort_values(ascending=False)

print(f"\n   Sales Frequency (Non-Zero Sales Days):")
for drug, freq in freq_series.items():
    print(f"      {drug}: {freq} days")

print(f"\n   ✅ Most frequently sold: {freq_series.index[0]} ({freq_series.iloc[0]} days)")

total_2017 = df_2017[drug_columns].sum().sort_values(ascending=False)
print(f"   ✅ Highest total sales: {total_2017.index[0]} ({total_2017.iloc[0]:,.2f} units)")

# Visualize
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

freq_series.plot(kind='bar', ax=axes[0], color='darkgreen', edgecolor='black')
axes[0].set_title('Sales Frequency in 2017\n(Non-Zero Sales Days)', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Drug Category', fontsize=11)
axes[0].set_ylabel('Number of Days with Sales', fontsize=11)
axes[0].tick_params(axis='x', rotation=45)
axes[0].grid(axis='y', alpha=0.3)

total_2017.plot(kind='bar', ax=axes[1], color='darkblue', edgecolor='black')
axes[1].set_title('Total Sales in 2017', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Drug Category', fontsize=11)
axes[1].set_ylabel('Total Sales Quantity', fontsize=11)
axes[1].tick_params(axis='x', rotation=45)
axes[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('output_q4_2017_sales.png', dpi=300, bbox_inches='tight')
print("\n   📊 Chart saved: output_q4_2017_sales.png")


# QUESTION 5: Drug Category with Highest Average Daily Sales

print("\n" + "="*60)
print("QUESTION 5: Average Daily Sales by Drug Category")
print("="*60)

avg_daily_sales = df[drug_columns].mean().sort_values(ascending=False)

for drug, avg_sales in avg_daily_sales.items():
    print(f"   {drug}: {avg_sales:.2f} units/day")

print(f"\n   ✅ Highest average daily sales: {avg_daily_sales.index[0]} ({avg_daily_sales.iloc[0]:.2f} units/day)")

# Visualize
plt.figure(figsize=(10, 6))
avg_daily_sales.plot(kind='bar', color='purple', edgecolor='black')
plt.title('Average Daily Sales by Drug Category', fontsize=16, fontweight='bold')
plt.xlabel('Drug Category (ATC Code)', fontsize=12)
plt.ylabel('Average Daily Sales Quantity', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('output_q5_avg_daily_sales.png', dpi=300, bbox_inches='tight')
print("\n   📊 Chart saved: output_q5_avg_daily_sales.png")


# QUESTION 6: Respiratory Drugs (R03) Seasonal Patterns

print("\n" + "="*60)
print("QUESTION 6: Respiratory Drugs (R03) Seasonal Analysis")
print("="*60)

r03_by_month = df.groupby('Month')['R03'].sum().sort_index()
r03_avg_by_month = df.groupby('Month')['R03'].mean().sort_index()

month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

print("\n   R03 Sales by Month:")
for month, sales in r03_by_month.items():
    print(f"      {month_names[month-1]}: {sales:,.2f} (Avg: {r03_avg_by_month[month]:.2f}/day)")

peak_month = r03_by_month.idxmax()
print(f"\n   ✅ Peak month: {month_names[peak_month-1]} (Total: {r03_by_month[peak_month]:,.2f})")
print(f"   ✅ Lowest month: {month_names[r03_by_month.idxmin()-1]} (Total: {r03_by_month.min():,.2f})")

# Visualize seasonal patterns
fig, axes = plt.subplots(2, 1, figsize=(12, 10))

axes[0].plot(range(1, 13), r03_by_month.values, marker='o', linewidth=2, 
             markersize=8, color='crimson', label='Total Sales')
axes[0].set_title('R03 (Respiratory Drugs) - Total Sales by Month', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Month', fontsize=11)
axes[0].set_ylabel('Total Sales Quantity', fontsize=11)
axes[0].set_xticks(range(1, 13))
axes[0].set_xticklabels(month_names)
axes[0].grid(True, alpha=0.3)
axes[0].legend()

axes[1].bar(range(1, 13), r03_avg_by_month.values, color='orange', edgecolor='black', alpha=0.7)
axes[1].set_title('R03 (Respiratory Drugs) - Average Daily Sales by Month', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Month', fontsize=11)
axes[1].set_ylabel('Average Daily Sales', fontsize=11)
axes[1].set_xticks(range(1, 13))
axes[1].set_xticklabels(month_names)
axes[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('output_q6_r03_seasonal.png', dpi=300, bbox_inches='tight')
print("\n   📊 Chart saved: output_q6_r03_seasonal.png")

# Year-over-year analysis
r03_by_year_month = df.groupby(['Year', 'Month'])['R03'].sum().reset_index()
r03_pivot = r03_by_year_month.pivot(index='Month', columns='Year', values='R03')

plt.figure(figsize=(12, 6))
for year in r03_pivot.columns:
    plt.plot(r03_pivot.index, r03_pivot[year], marker='o', linewidth=2, label=str(year))

plt.title('R03 (Respiratory Drugs) - Sales Trends Across Years', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Sales Quantity', fontsize=12)
plt.xticks(range(1, 13), month_names)
plt.legend(title='Year', fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('output_q6_r03_yearly_trends.png', dpi=300, bbox_inches='tight')
print("   📊 Chart saved: output_q6_r03_yearly_trends.png")


# SUMMARY

print("\n" + "="*60)
print("ANALYSIS COMPLETE!")
print("="*60)
print("\n📊 All charts have been saved to the current directory")
print("✅ All 6 questions answered successfully")
print("\nKey Findings:")
print(f"   • Highest total sales: {total_sales.index[0]} ({total_sales.iloc[0]:,.2f} units)")
print(f"   • Highest avg daily sales: {avg_daily_sales.index[0]} ({avg_daily_sales.iloc[0]:.2f} units/day)")
print(f"   • Most frequent in 2017: {freq_series.index[0]} ({freq_series.iloc[0]} days)")
print(f"   • R03 peak month: {month_names[peak_month-1]}")
print("="*60)
