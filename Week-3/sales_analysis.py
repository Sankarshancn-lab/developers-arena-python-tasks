# ============================================================
# WEEK 3 - SALES DATA ANALYSIS
# Developers Arena Python Internship
#
# Day 1: Data Loading
# Day 2: Data Exploration
# Day 3: Data Cleaning
# Day 4: Sales Analysis
# ============================================================

import pandas as pd


# ============================================================
# DAY 1: LOAD DATASET
# ============================================================

# Load the official Developers Arena sales dataset
df = pd.read_csv("sales_data.csv")

print("\n========== ORIGINAL SALES DATA ==========")
print(df.head())

# Display dataset information
print("\n========== DATASET INFORMATION ==========")
df.info()

# Display dataset dimensions
print("\n========== DATASET SHAPE ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Display column names
print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())


# ============================================================
# DAY 2: DATA EXPLORATION
# ============================================================

# Display statistical summary
print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

# Check missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Check duplicate records
print("\n========== DUPLICATE RECORDS ==========")
print("Duplicate Rows:", df.duplicated().sum())

# Explore unique products
print("\n========== UNIQUE PRODUCTS ==========")
print(df["Product"].unique())

# Count transactions for each product
print("\n========== PRODUCT COUNTS ==========")
print(df["Product"].value_counts())

# Analyze total sales by region
print("\n========== SALES BY REGION ==========")
sales_by_region = df.groupby("Region")["Total_Sales"].sum()

print(sales_by_region)

# Analyze total sales by product
print("\n========== SALES BY PRODUCT ==========")
sales_by_product = df.groupby("Product")["Total_Sales"].sum()

print(sales_by_product)

# Count unique customers
print("\n========== CUSTOMER ANALYSIS ==========")
print("Total Unique Customers:", df["Customer_ID"].nunique())


# ============================================================
# DAY 3: DATA CLEANING
# ============================================================

print("\n========== DAY 3: DATA CLEANING ==========")

# Step 1: Display missing values before cleaning

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())


# Step 2: Remove exact duplicate records

initial_rows = df.shape[0]

df = df.drop_duplicates()

duplicates_removed = initial_rows - df.shape[0]

print("\nDuplicate Records Removed:", duplicates_removed)


# Step 3: Handle missing numerical values

# Fill missing Quantity using median
if df["Quantity"].isnull().any():
    df["Quantity"] = df["Quantity"].fillna(
        df["Quantity"].median()
    )

# Fill missing Price using median
if df["Price"].isnull().any():
    df["Price"] = df["Price"].fillna(
        df["Price"].median()
    )


# Step 4: Handle missing categorical values

# Fill missing Product using mode
if df["Product"].isnull().any():
    df["Product"] = df["Product"].fillna(
        df["Product"].mode()[0]
    )

# Fill missing Region using mode
if df["Region"].isnull().any():
    df["Region"] = df["Region"].fillna(
        df["Region"].mode()[0]
    )

# Handle missing customer identifiers
df["Customer_ID"] = df["Customer_ID"].fillna("UNKNOWN")


# Step 5: Convert Date column into datetime format

df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)


# Step 6: Validate numerical columns

df["Quantity"] = pd.to_numeric(
    df["Quantity"],
    errors="coerce"
)

df["Price"] = pd.to_numeric(
    df["Price"],
    errors="coerce"
)

# Remove records with invalid dates or numerical values
df = df.dropna(
    subset=["Date", "Quantity", "Price"]
)

# Remove invalid numerical records
df = df[
    (df["Quantity"] > 0) &
    (df["Price"] >= 0)
].copy()


# Step 7: Recalculate Total Sales

# Total Sales = Quantity * Price

df["Total_Sales"] = df["Quantity"] * df["Price"]


# Step 8: Check missing values after cleaning

print("\n========== MISSING VALUES AFTER CLEANING ==========")
print(df.isnull().sum())


# Step 9: Check duplicate records after cleaning

print("\n========== DUPLICATES AFTER CLEANING ==========")
print("Duplicate Rows:", df.duplicated().sum())


# Step 10: Display cleaned dataset

print("\n========== CLEANED SALES DATA ==========")
print(df.head(10))


# Step 11: Display final dataset information

print("\n========== CLEANED DATASET INFORMATION ==========")
df.info()


# Step 12: Display final dataset shape

print("\n========== FINAL DATASET SHAPE ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# Step 13: Save cleaned dataset

df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaned dataset saved successfully!")


# ============================================================
# DAY 4: SALES DATA ANALYSIS
# ============================================================

print("\n========== DAY 4: SALES ANALYSIS ==========")


# 1. Calculate total revenue

total_revenue = df["Total_Sales"].sum()

print("\n========== TOTAL REVENUE ==========")
print(f"Rs. {total_revenue:,.2f}")


# 2. Calculate total units sold

total_units = df["Quantity"].sum()

print("\n========== TOTAL UNITS SOLD ==========")
print(total_units)


# 3. Find best-selling product by quantity

product_quantity = df.groupby("Product")["Quantity"].sum()

best_selling_product = product_quantity.idxmax()

print("\n========== BEST-SELLING PRODUCT ==========")
print("Product:", best_selling_product)

print("\nProduct-wise Quantity Sold:")
print(product_quantity.sort_values(ascending=False))


# 4. Find highest revenue-generating product

product_revenue = df.groupby("Product")["Total_Sales"].sum()

highest_revenue_product = product_revenue.idxmax()

print("\n========== HIGHEST REVENUE PRODUCT ==========")
print("Product:", highest_revenue_product)

print("\nProduct-wise Revenue:")
print(product_revenue.sort_values(ascending=False))


# 5. Calculate average transaction value

average_transaction = df["Total_Sales"].mean()

print("\n========== AVERAGE TRANSACTION VALUE ==========")
print(f"Rs. {average_transaction:,.2f}")


# 6. Find highest sales transaction

highest_sale = df.loc[df["Total_Sales"].idxmax()]

print("\n========== HIGHEST SALES TRANSACTION ==========")
print(highest_sale)


# 7. Find lowest sales transaction

lowest_sale = df.loc[df["Total_Sales"].idxmin()]

print("\n========== LOWEST SALES TRANSACTION ==========")
print(lowest_sale)


# 8. Calculate region-wise revenue

region_revenue = df.groupby("Region")["Total_Sales"].sum()

print("\n========== REGION-WISE REVENUE ==========")
print(region_revenue.sort_values(ascending=False))


# 9. Find highest-performing region

best_region = region_revenue.idxmax()

print("\n========== HIGHEST-PERFORMING REGION ==========")
print(best_region)


# 10. Calculate average revenue per product

average_product_revenue = product_revenue.mean()

print("\n========== AVERAGE REVENUE PER PRODUCT ==========")
print(f"Rs. {average_product_revenue:,.2f}")


# 11. Calculate monthly sales

df["Month"] = df["Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Total_Sales"].sum()

print("\n========== MONTHLY SALES ==========")
print(monthly_sales)


# 12. Find highest-performing month

best_month = monthly_sales.idxmax()

print("\n========== HIGHEST-PERFORMING MONTH ==========")
print(best_month)


# 13. Customer analysis

unique_customers = df["Customer_ID"].nunique()

print("\n========== CUSTOMER ANALYSIS ==========")
print("Total Unique Customers:", unique_customers)


# 14. Calculate average quantity per transaction

average_quantity = df["Quantity"].mean()

print("\n========== AVERAGE QUANTITY PER TRANSACTION ==========")
print(round(average_quantity, 2))


# ============================================================
# FINAL BUSINESS SUMMARY
# ============================================================

print("\n========== FINAL BUSINESS SUMMARY ==========")

print(f"Total Revenue: Rs. {total_revenue:,.2f}")

print(f"Total Units Sold: {total_units}")

print(f"Total Transactions: {len(df)}")

print(f"Unique Customers: {unique_customers}")

print(f"Best-Selling Product: {best_selling_product}")

print(f"Highest Revenue Product: {highest_revenue_product}")

print(f"Average Transaction Value: Rs. {average_transaction:,.2f}")

print(f"Best Performing Region: {best_region}")

print(f"Highest Performing Month: {best_month}")

print("\n========== DAY 4 ANALYSIS COMPLETED ==========")