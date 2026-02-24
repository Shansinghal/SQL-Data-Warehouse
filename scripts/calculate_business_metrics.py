import pandas as pd
import os
import numpy as np

base_dir = r"c:\Users\Shant\OneDrive\Desktop\sql-data-warehouse-project\datasets"

# Load sales data
crm_sales = pd.read_csv(os.path.join(base_dir, "source_crm", "sales_details.csv"))
# Load product data for some extra context if needed
crm_prd = pd.read_csv(os.path.join(base_dir, "source_crm", "prd_info.csv"))

print("--- Business Performance Metrics ---")

# 1. Total Revenue & Quantity
# In SQL, sales are represented by sls_sales. Let's calculate total revenue.
# Clean data based on SQL logic (sales = quantity * price if invalid)
crm_sales['sls_price_abs'] = crm_sales['sls_price'].abs()
crm_sales['calculated_sales'] = crm_sales['sls_quantity'] * crm_sales['sls_price_abs']

# Handle cases where sls_sales is null or <= 0 or doesn't match
mask = crm_sales['sls_sales'].isnull() | (crm_sales['sls_sales'] <= 0) | (crm_sales['sls_sales'] != crm_sales['calculated_sales'])
crm_sales.loc[mask, 'sls_sales'] = crm_sales.loc[mask, 'calculated_sales']

total_revenue = crm_sales['sls_sales'].sum()
total_items_sold = crm_sales['sls_quantity'].sum()
unique_products_sold = crm_sales['sls_prd_key'].nunique()
unique_orders = crm_sales['sls_ord_num'].nunique()

print(f"Total Revenue Generated: ${total_revenue:,.2f}")
print(f"Total Items Sold: {total_items_sold:,}")
print(f"Unique Orders Processed: {unique_orders:,}")
print(f"Unique Products Sold: {unique_products_sold:,}")

# 2. Data Cleansing Metrics
rows_fixed = mask.sum()
print(f"Data Anomalies Cleansed (Sales Calculation Fixed): {rows_fixed:,} rows")

# 3. Date Range
# Convert dates which are integers e.g. 20190101
valid_dates = crm_sales[crm_sales['sls_order_dt'] > 0]['sls_order_dt'].astype(str)
valid_dates = pd.to_datetime(valid_dates, format='%Y%m%d', errors='coerce')
min_date = valid_dates.min().strftime('%Y-%m-%d')
max_date = valid_dates.max().strftime('%Y-%m-%d')
print(f"Data Timeline: {min_date} to {max_date}")
