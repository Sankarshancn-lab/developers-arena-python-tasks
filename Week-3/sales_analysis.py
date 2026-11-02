
# ============================================================
# WEEK 3 - SALES DATA ANALYSIS
# Developers Arena Python Internship
# Day 1: Data Loading
# Day 2: Data Exploration
# Day 3: Data Cleaning
# ============================================================

import pandas as pd

# ------------------------------------------------------------
# DAY 1: LOAD DATASET
# ------------------------------------------------------------

df = pd.read_csv("sales_data.csv")

print("\n========== ORIGINAL SALES DATA ==========")
print(df.head())

print("\n========== DATASET INFORMATION ==========")
df.info()

print("\n========== DATASET SHAPE ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# ------------------------------------------------------------
# DAY 2: DATA EXPLORATION
# ------------------------------------------------------------

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATE RECORDS ==========")
print("Duplicate Rows:", df.duplicated().sum())

print("\n========== UNIQUE PRODUCTS ==========")
print(df["Product"].unique())

print("\n========== PRODUCT COUNTS ==========")
print(df["Product"].value_counts())

print("\n========== SALES BY REGION ==========")
print(df.groupby("Region")["Total_Sales"].sum())

print("\n========== SALES BY CATEGORY ==========")
print(df.groupby("Category")["Total_Sales"].sum())


# ============================================================
# DAY 3: DATA CLEANING - IMPROVED VERSION
# ============================================================

print("\n========== DAY 3: DATA CLEANING ==========")

# Step 1: Remove duplicate transactions
df = df.drop_duplicates(subset="Order_ID", keep="first")

# Step 2: Handle missing numerical values
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())

# Step 3: Handle missing categorical values
df["Region"] = df["Region"].fillna(df["Region"].mode()[0])

# Step 4: Convert date column into datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

# Step 5: Validate numerical columns
df = df.dropna(subset=["Order_ID", "Order_Date", "Unit_Price"])

df = df[
    (df["Quantity"] > 0) &
    (df["Unit_Price"] >= 0)
].copy()

# Step 6: Recalculate sales
df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

# Step 7: Verify missing values
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Step 8: Verify duplicates
print("\nDuplicate Records:")
print(df.duplicated(subset="Order_ID").sum())

# Step 9: Display cleaned dataset
print("\nCleaned Dataset:")
print(df)

# Step 10: Display final information
print("\nFinal Dataset Information:")
df.info()

print("\nFinal Dataset Shape:", df.shape)

# Step 11: Save cleaned dataset
df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaned dataset saved successfully!")
# ============================================================
# DAY 4: SALES DATA ANALYSIS
# ============================================================

print("\n========== DAY 4: SALES ANALYSIS ==========")

# 1. Calculate total revenue

total_revenue = df["Total_Sales"].sum()

print("\nTOTAL REVENUE:")
print(f"Rs. {total_revenue:,.2f}")


# 2. Calculate total units sold

total_units = df["Quantity"].sum()

print("\nTOTAL UNITS SOLD:")
print(total_units)


# 3. Find best-selling product by quantity

product_quantity = df.groupby("Product")["Quantity"].sum()

best_selling_product = product_quantity.idxmax()

print("\nBEST-SELLING PRODUCT BY QUANTITY:")
print(best_selling_product)

print("\nPRODUCT-WISE QUANTITY SOLD:")
print(product_quantity)


# 4. Find highest revenue-generating product

product_revenue = df.groupby("Product")["Total_Sales"].sum()

highest_revenue_product = product_revenue.idxmax()

print("\nHIGHEST REVENUE-GENERATING PRODUCT:")
print(highest_revenue_product)

print("\nPRODUCT-WISE REVENUE:")
print(product_revenue)


# 5. Calculate average transaction value

average_transaction = df["Total_Sales"].mean()

print("\nAVERAGE TRANSACTION VALUE:")
print(f"Rs. {average_transaction:,.2f}")


# 6. Find highest sales transaction

highest_sale = df.loc[df["Total_Sales"].idxmax()]

print("\nHIGHEST SALES TRANSACTION:")
print(highest_sale)


# 7. Find lowest sales transaction

lowest_sale = df.loc[df["Total_Sales"].idxmin()]

print("\nLOWEST SALES TRANSACTION:")
print(lowest_sale)


# 8. Calculate region-wise revenue

region_revenue = df.groupby("Region")["Total_Sales"].sum()

print("\nREGION-WISE REVENUE:")
print(region_revenue)


# 9. Find highest-performing region

best_region = region_revenue.idxmax()

print("\nHIGHEST-PERFORMING REGION:")
print(best_region)


# 10. Calculate category-wise revenue

category_revenue = df.groupby("Category")["Total_Sales"].sum()

print("\nCATEGORY-WISE REVENUE:")
print(category_revenue)


# 11. Find highest-performing category

best_category = category_revenue.idxmax()

print("\nHIGHEST-PERFORMING CATEGORY:")
print(best_category)


# 12. Calculate average revenue per product

print("\nAVERAGE REVENUE PER PRODUCT:")
print(product_revenue.mean())


# 13. Display final business summary

print("\n========== BUSINESS SUMMARY ==========")

print(f"Total Revenue: Rs. {total_revenue:,.2f}")
print(f"Total Units Sold: {total_units}")
print(f"Best-Selling Product: {best_selling_product}")
print(f"Highest Revenue Product: {highest_revenue_product}")
print(f"Average Transaction Value: Rs. {average_transaction:,.2f}")
print(f"Best Performing Region: {best_region}")
print(f"Best Performing Category: {best_category}")

print("\n========== DAY 4 ANALYSIS COMPLETED ==========")

