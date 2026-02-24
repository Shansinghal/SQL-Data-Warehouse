import pandas as pd
import os

base_dir = r"c:\Users\Shant\OneDrive\Desktop\sql-data-warehouse-project\datasets"

# CRM Data
crm_cust = pd.read_csv(os.path.join(base_dir, "source_crm", "cust_info.csv"))
crm_prd = pd.read_csv(os.path.join(base_dir, "source_crm", "prd_info.csv"))
crm_sales = pd.read_csv(os.path.join(base_dir, "source_crm", "sales_details.csv"))

# ERP Data
erp_cust = pd.read_csv(os.path.join(base_dir, "source_erp", "CUST_AZ12.csv"))
erp_loc = pd.read_csv(os.path.join(base_dir, "source_erp", "LOC_A101.csv"))
erp_cat = pd.read_csv(os.path.join(base_dir, "source_erp", "PX_CAT_G1V2.csv"))

total_rows = len(crm_cust) + len(crm_prd) + len(crm_sales) + len(erp_cust) + len(erp_loc) + len(erp_cat)
print(f"--- Dataset Metrics ---")
print(f"Total files: 6")
print(f"Total rows integrated: {total_rows:,}")
print(f"CRM Customers: {len(crm_cust):,}")
print(f"ERP Customers: {len(erp_cust):,}")
print(f"Sales Records: {len(crm_sales):,}")
