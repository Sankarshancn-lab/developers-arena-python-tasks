"""
Project: E-commerce Sales Analysis and Visualization
Internship: Developers Arena - Week 4

Description:
A complete data analysis pipeline using Pandas, NumPy
and Matplotlib.

Features:
1. Data loading
2. Data exploration
3. Data cleaning
4. Data validation
5. Sales analysis
6. Data visualization
7. Exporting cleaned data and visualizations
8. Automated Markdown report generation
"""

import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. PROJECT CONFIGURATION
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(
    BASE_DIR, "data", "sales_data.csv"
)

CLEANED_DATA_PATH = os.path.join(
    BASE_DIR, "data", "cleaned_sales_data.csv"
)

VISUALIZATION_DIR = os.path.join(
    BASE_DIR, "visualizations"
)

REPORT_DIR = os.path.join(
    BASE_DIR, "report"
)

REPORT_PATH = os.path.join(
    REPORT_DIR, "analysis_report.md"
)

REQUIRED_COLUMNS = [
    "Date",
    "Product",
    "Quantity",
    "Price",
    "Customer_ID",
    "Region",
    "Total_Sales"
]


# ============================================================
# 2. DIRECTORY VALIDATION
# ============================================================

def create_directories():
    """
    Create required project directories
    if they do not already exist.
    """

    os.makedirs(VISUALIZATION_DIR, exist_ok=True)
    os.makedirs(REPORT_DIR, exist_ok=True)

    print("\nProject directories verified successfully.")


# ============================================================
# 3. DATA LOADING
# ============================================================

def load_data(file_path):
    """
    Load the sales dataset from a CSV file.
    """

    try:

        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"Dataset not found: {file_path}"
            )

        df = pd.read_csv(file_path)

        if df.empty:
            raise ValueError(
                "The dataset is empty."
            )

        print("\n========== DATA LOADING ==========")

        print("Dataset loaded successfully.")
        print("Rows:", df.shape[0])
        print("Columns:", df.shape[1])

        return df

    except (
        FileNotFoundError,
        pd.errors.EmptyDataError,
        pd.errors.ParserError,
        ValueError
    ) as error:

        print("Data loading error:", error)
        sys.exit(1)


# ============================================================
# 4. DATA VALIDATION
# ============================================================

def validate_columns(df):
    """
    Verify that all required columns exist.
    """

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:

        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    print("\nColumn validation successful.")


# ============================================================
# 5. DATA EXPLORATION
# ============================================================

def explore_data(df):
    """
    Explore dataset structure and statistical information.
    """

    print("\n========== DATA EXPLORATION ==========")

    print("\nFirst five records:")
    print(df.head())

    print("\nDataset information:")
    df.info()

    print("\nStatistical summary:")
    print(df.describe(include="all"))

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDuplicate records:")
    print(df.duplicated().sum())


# ============================================================
# 6. DATA CLEANING
# ============================================================

def clean_data(df):
    """
    Clean and preprocess the sales dataset.
    """

    print("\n========== DATA CLEANING ==========")

    df = df.copy()

    # --------------------------------------------------------
    # Remove duplicate records
    # --------------------------------------------------------

    initial_rows = len(df)

    df.drop_duplicates(inplace=True)

    removed_duplicates = initial_rows - len(df)

    # --------------------------------------------------------
    # Convert date column
    # --------------------------------------------------------

    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce"
    )

    # --------------------------------------------------------
    # Convert numeric columns
    # --------------------------------------------------------

    numeric_columns = [
        "Quantity",
        "Price",
        "Total_Sales"
    ]

    for column in numeric_columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    # --------------------------------------------------------
    # Handle missing categorical values
    # --------------------------------------------------------

    categorical_columns = [
        "Product",
        "Customer_ID",
        "Region"
    ]

    for column in categorical_columns:

        df[column] = df[column].replace(
            r"^\s*$",
            np.nan,
            regex=True
        )

        if df[column].isnull().any():

            mode_values = df[column].mode()

            if mode_values.empty:

                raise ValueError(
                    f"Cannot impute missing values in {column}."
                )

            df[column] = df[column].fillna(
                mode_values[0]
            )

    # --------------------------------------------------------
    # Remove records with invalid dates
    # --------------------------------------------------------

    df.dropna(
        subset=["Date"],
        inplace=True
    )

    # --------------------------------------------------------
    # Handle missing numeric values
    # --------------------------------------------------------

    for column in ["Quantity", "Price"]:

        if df[column].isnull().any():

            median_value = df[column].median()

            if pd.isna(median_value):

                raise ValueError(
                    f"Cannot calculate median for {column}."
                )

            df[column] = df[column].fillna(
                median_value
            )

    # --------------------------------------------------------
    # Remove invalid sales records
    # --------------------------------------------------------

    df = df[
        (df["Quantity"] > 0) &
        (df["Price"] >= 0)
    ].copy()

    if df.empty:

        raise ValueError(
            "No valid records remain after cleaning."
        )

    # --------------------------------------------------------
    # Recalculate total sales
    # --------------------------------------------------------

    df["Total_Sales"] = (
        df["Quantity"] * df["Price"]
    )

    # --------------------------------------------------------
    # Final data validation
    # --------------------------------------------------------

    if df.isnull().any().any():

        raise ValueError(
            "Missing values remain after cleaning."
        )

    numeric_data = df[
        ["Quantity", "Price", "Total_Sales"]
    ].to_numpy()

    if not np.isfinite(numeric_data).all():

        raise ValueError(
            "Non-finite numeric values detected."
        )

    # --------------------------------------------------------
    # Export cleaned dataset
    # --------------------------------------------------------

    df.to_csv(
        CLEANED_DATA_PATH,
        index=False
    )

    print("Removed duplicate records:", removed_duplicates)
    print("Final cleaned records:", len(df))

    print(
        "Remaining missing values:",
        df.isnull().sum().sum()
    )

    print("Cleaned dataset saved successfully.")

    return df


# ============================================================
# 7. BASIC DATA ANALYSIS
# ============================================================

def analyze_data(df):
    """
    Calculate important sales performance metrics.
    """

    print("\n========== SALES ANALYSIS ==========")

    # Total revenue
    total_revenue = df["Total_Sales"].sum()

    # Total units sold
    total_units = df["Quantity"].sum()

    # Average transaction value
    average_transaction = df["Total_Sales"].mean()

    # Product-wise quantity
    product_quantity = (
        df.groupby("Product")["Quantity"]
        .sum()
        .sort_values(ascending=False)
    )

    # Product-wise revenue
    product_revenue = (
        df.groupby("Product")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    # Region-wise revenue
    region_revenue = (
        df.groupby("Region")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    # Monthly revenue
    monthly_revenue = (
        df.groupby(
            df["Date"].dt.to_period("M")
        )["Total_Sales"]
        .sum()
    )

    # Unique customers
    unique_customers = df["Customer_ID"].nunique()

    # --------------------------------------------------------
    # Display results
    # --------------------------------------------------------

    print(
        f"\nTotal Revenue: ₹{total_revenue:,.2f}"
    )

    print(
        "Total Units Sold:",
        total_units
    )

    print(
        f"Average Transaction Value: ₹{average_transaction:,.2f}"
    )

    print(
        "Unique Customers:",
        unique_customers
    )

    print("\nProduct-wise Quantity Sold:")
    print(product_quantity)

    print("\nProduct-wise Revenue:")
    print(product_revenue)

    print("\nRegion-wise Revenue:")
    print(region_revenue)

    print("\nMonthly Revenue:")
    print(monthly_revenue)

    print(
        "\nBest-selling Product:",
        product_quantity.idxmax()
    )

    print(
        "Highest Revenue Product:",
        product_revenue.idxmax()
    )

    print(
        "Highest Revenue Region:",
        region_revenue.idxmax()
    )

    print(
        "Highest Revenue Month:",
        monthly_revenue.idxmax()
    )

    # Return results for visualization and reporting.
    return {
        "total_revenue": total_revenue,
        "total_units": total_units,
        "average_transaction": average_transaction,
        "unique_customers": unique_customers,
        "product_quantity": product_quantity,
        "product_revenue": product_revenue,
        "region_revenue": region_revenue,
        "monthly_revenue": monthly_revenue
    }


# ============================================================
# 8. DATA VISUALIZATION
# ============================================================

def create_visualizations(results):
    """
    Generate professional sales visualizations
    using Matplotlib.
    """

    print("\n========== DATA VISUALIZATION ==========")

    try:

        # ====================================================
        # CHART 1: PRODUCT-WISE REVENUE BAR CHART
        # ====================================================

        product_revenue = results["product_revenue"]

        plt.figure(figsize=(10, 6))

        bars = plt.bar(
            product_revenue.index,
            product_revenue.values
        )

        plt.title(
            "Product-wise Revenue Analysis",
            fontsize=16,
            fontweight="bold"
        )

        plt.xlabel(
            "Products",
            fontsize=12
        )

        plt.ylabel(
            "Revenue (₹)",
            fontsize=12
        )

        plt.xticks(rotation=20)

        plt.grid(
            axis="y",
            linestyle="--",
            alpha=0.5
        )

        # Display revenue values above bars.
        for bar in bars:

            height = bar.get_height()

            plt.text(
                bar.get_x() + bar.get_width() / 2,
                height,
                f"₹{height:,.0f}",
                ha="center",
                va="bottom",
                fontsize=9
            )

        plt.tight_layout()

        plt.savefig(
            os.path.join(
                VISUALIZATION_DIR,
                "product_sales_bar.png"
            ),
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        print("Product revenue bar chart saved.")

        # ====================================================
        # CHART 2: MONTHLY SALES LINE CHART
        # ====================================================

        monthly_revenue = results["monthly_revenue"]

        plt.figure(figsize=(10, 6))

        plt.plot(
            monthly_revenue.index.astype(str),
            monthly_revenue.values,
            marker="o",
            linewidth=2,
            markersize=8
        )

        plt.title(
            "Monthly Sales Revenue Trend",
            fontsize=16,
            fontweight="bold"
        )

        plt.xlabel(
            "Month",
            fontsize=12
        )

        plt.ylabel(
            "Revenue (₹)",
            fontsize=12
        )

        plt.grid(
            True,
            linestyle="--",
            alpha=0.5
        )

        # Display revenue values near each point.
        for x, y in enumerate(monthly_revenue.values):

            plt.annotate(
                f"₹{y:,.0f}",
                (x, y),
                textcoords="offset points",
                xytext=(0, 10),
                ha="center",
                fontsize=9
            )

        plt.tight_layout()

        plt.savefig(
            os.path.join(
                VISUALIZATION_DIR,
                "monthly_sales_line.png"
            ),
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        print("Monthly sales line chart saved.")

        # ====================================================
        # CHART 3: REGIONAL REVENUE PIE CHART
        # ====================================================

        region_revenue = results["region_revenue"]

        plt.figure(figsize=(9, 7))

        plt.pie(
            region_revenue.values,
            labels=region_revenue.index,
            autopct="%1.1f%%",
            startangle=90,
            shadow=False,
            textprops={
                "fontsize": 11
            }
        )

        plt.title(
            "Regional Revenue Distribution",
            fontsize=16,
            fontweight="bold"
        )

        plt.axis("equal")

        plt.tight_layout()

        plt.savefig(
            os.path.join(
                VISUALIZATION_DIR,
                "regional_sales_pie.png"
            ),
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        print("Regional revenue pie chart saved.")

        print(
            "\nAll three visualizations generated successfully."
        )

    except (KeyError, ValueError, OSError) as error:

        plt.close("all")

        raise RuntimeError(
            f"Visualization generation failed: {error}"
        ) from error


# ============================================================
# 9. AUTOMATED REPORT GENERATION
# ============================================================

def generate_report(df, results):
    """
    Generate a professional Markdown report containing
    numerical analysis, business insights and visualizations.
    """

    print("\n========== REPORT GENERATION ==========")

    # Extract important metrics.
    total_revenue = results["total_revenue"]
    total_units = results["total_units"]
    average_transaction = results["average_transaction"]
    unique_customers = results["unique_customers"]

    product_revenue = results["product_revenue"]
    product_quantity = results["product_quantity"]
    region_revenue = results["region_revenue"]
    monthly_revenue = results["monthly_revenue"]

    # Identify top-performing categories.
    best_selling_product = product_quantity.idxmax()
    highest_revenue_product = product_revenue.idxmax()
    highest_revenue_region = region_revenue.idxmax()
    highest_revenue_month = monthly_revenue.idxmax()

    # Dataset information.
    total_records = len(df)
    total_columns = len(df.columns)

    start_date = df["Date"].min().strftime("%d %B %Y")
    end_date = df["Date"].max().strftime("%d %B %Y")

    missing_values = int(df.isnull().sum().sum())
    duplicate_records = int(df.duplicated().sum())

    # Create product revenue table.
    product_table = ""

    for product, revenue in product_revenue.items():

        quantity = product_quantity[product]

        product_table += (
            f"| {product} | {quantity} | ₹{revenue:,.2f} |\n"
        )

    # Create regional revenue table.
    region_table = ""

    for region, revenue in region_revenue.items():

        percentage = (revenue / total_revenue) * 100

        region_table += (
            f"| {region} | ₹{revenue:,.2f} | {percentage:.2f}% |\n"
        )

    # Create monthly revenue table.
    monthly_table = ""

    for month, revenue in monthly_revenue.items():

        monthly_table += (
            f"| {month} | ₹{revenue:,.2f} |\n"
        )

    # Calculate business contribution percentages.
    top_product_share = (
        product_revenue.max() / total_revenue
    ) * 100

    top_region_share = (
        region_revenue.max() / total_revenue
    ) * 100

    # Generate Markdown report.
    report = f"""
# E-commerce Sales Analysis and Visualization

**Developers Arena Python Internship – Week 4**

---

## 1. Project Overview

This project analyses e-commerce sales transaction data using Python,
Pandas, NumPy and Matplotlib.

The objective is to identify product performance, regional revenue
distribution, monthly sales trends and important business insights.

The project implements a complete data analysis workflow, including
data loading, exploration, cleaning, validation, statistical analysis,
visualization and automated report generation.

## 2. Dataset Description

| Attribute | Details |
|---|---|
| Dataset | E-commerce Sales Data |
| Total Records | {total_records} |
| Total Columns | {total_columns} |
| Starting Date | {start_date} |
| Ending Date | {end_date} |
| Unique Customers | {unique_customers} |

### Dataset Columns

| Column | Description |
|---|---|
| Date | Transaction date |
| Product | Product purchased |
| Quantity | Number of units purchased |
| Price | Unit price |
| Customer_ID | Customer identification |
| Region | Sales region |
| Total_Sales | Total transaction value |

## 3. Data Cleaning and Validation

The following preprocessing operations were implemented:

- Checked the dataset for missing values.
- Identified and removed exact duplicate records.
- Converted the Date column into datetime format.
- Converted numeric columns into appropriate numeric types.
- Implemented mode imputation for missing categorical values.
- Implemented median imputation for missing numerical values.
- Removed invalid dates and non-positive quantities.
- Recalculated transaction revenue using Quantity × Price.
- Validated numeric values before analysis.

### Data Quality Summary

| Validation | Result |
|---|---:|
| Records after cleaning | {total_records} |
| Missing values remaining | {missing_values} |
| Duplicate records remaining | {duplicate_records} |

The supplied dataset contained no missing values or duplicate
records, so no imputation or duplicate removal was necessary.

## 4. Key Business Metrics

| Metric | Result |
|---|---:|
| Total Revenue | ₹{total_revenue:,.2f} |
| Total Units Sold | {total_units} |
| Average Transaction Value | ₹{average_transaction:,.2f} |
| Unique Customers | {unique_customers} |
| Best-Selling Product | {best_selling_product} |
| Highest Revenue Product | {highest_revenue_product} |
| Highest Revenue Region | {highest_revenue_region} |
| Highest Revenue Month | {highest_revenue_month} |

## 5. Product Performance Analysis

The following table compares product-wise sales quantity and revenue.

| Product | Units Sold | Revenue |
|---|---:|---:|
{product_table}

### Product Revenue Visualization

![Product-wise Revenue Analysis](../visualizations/product_sales_bar.png)

### Product Insights

- {best_selling_product} recorded the highest sales quantity.
- {highest_revenue_product} generated the highest revenue.
- The highest-revenue product contributed approximately
  {top_product_share:.2f}% of total revenue.
- Product performance can help businesses prioritize inventory
  and marketing activities.

## 6. Regional Sales Analysis

The following table presents revenue generated across different regions.

| Region | Revenue | Revenue Share |
|---|---:|---:|
{region_table}

### Regional Revenue Visualization

![Regional Revenue Distribution](../visualizations/regional_sales_pie.png)

### Regional Insights

- {highest_revenue_region} generated the highest regional revenue.
- This region contributed approximately {top_region_share:.2f}%
  of total revenue.
- Regional performance differences can help businesses identify
  opportunities for targeted marketing and sales improvement.

## 7. Monthly Sales Trend Analysis

The monthly revenue distribution is shown below.

| Month | Revenue |
|---|---:|
{monthly_table}

### Monthly Sales Visualization

![Monthly Sales Revenue Trend](../visualizations/monthly_sales_line.png)

### Monthly Insights

- {highest_revenue_month} recorded the highest revenue.
- Monthly comparisons help identify changes in sales performance.
- April contains data only up to 9 April 2024, so it represents
  a partial month and should not be compared directly with
  complete months.

## 8. Business Recommendations

Based on the analysis, the following recommendations can be considered:

1. **Product Strategy:** Prioritize inventory planning for
   {best_selling_product}, which recorded the highest sales quantity.

2. **Regional Strategy:** Investigate the successful sales patterns
   in {highest_revenue_region} and identify opportunities to improve
   performance in other regions.

3. **Sales Monitoring:** Track monthly revenue to identify
   performance changes and potential seasonal patterns.

4. **Business Intelligence:** Use product-wise and regional
   performance metrics to support data-driven business decisions.

## 9. Technologies Used

| Technology | Application |
|---|---|
| Python | Main programming language |
| Pandas | Data processing and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| CSV | Dataset storage |
| Git and GitHub | Version control |

## 10. Project Workflow

1. Load the sales dataset.
2. Explore the dataset structure and statistics.
3. Validate required columns.
4. Clean and preprocess the data.
5. Calculate business performance metrics.
6. Generate bar, line and pie charts.
7. Export the cleaned dataset.
8. Generate this automated analysis report.

## 11. Conclusion

The project successfully analysed {total_records} e-commerce
transactions and identified important patterns in product,
regional and monthly sales performance.

The analysis generated total revenue of ₹{total_revenue:,.2f}
across {total_units} units sold.

{best_selling_product} was the best-selling product, while
{highest_revenue_region} generated the highest regional revenue.

The project demonstrates how Python-based data analysis and
visualization can transform raw sales data into meaningful
business insights.

---

**Report generated automatically using Python, Pandas and Matplotlib.**
"""

    # Save report.
    with open(
        REPORT_PATH,
        "w",
        encoding="utf-8"
    ) as report_file:

        report_file.write(report)

    print("Analysis report generated successfully.")
    print("Report location:", REPORT_PATH)


# ============================================================
# 10. MAIN EXECUTION
# ============================================================

def main():
    """
    Execute the complete data analysis pipeline.
    """

    print("=" * 60)

    print(
        " E-COMMERCE SALES ANALYSIS AND VISUALIZATION "
    )

    print("=" * 60)

    # Create project directories.
    create_directories()

    # Stage 1: Load dataset.
    df = load_data(DATA_PATH)

    # Stage 2: Validate dataset structure.
    validate_columns(df)

    # Stage 3: Explore dataset.
    explore_data(df)

    # Stage 4: Clean dataset.
    cleaned_df = clean_data(df)

    # Stage 5: Perform sales analysis.
    results = analyze_data(cleaned_df)

    # Stage 6: Generate visualizations.
    create_visualizations(results)

    # Stage 7: Generate automated report.
    generate_report(cleaned_df, results)

    # --------------------------------------------------------
    # Final pipeline status
    # --------------------------------------------------------

    print("\n========== PIPELINE STATUS ==========")

    print("Data loading: SUCCESS")
    print("Data validation: SUCCESS")
    print("Data exploration: SUCCESS")
    print("Data cleaning: SUCCESS")
    print("Sales analysis: SUCCESS")
    print("Data visualization: SUCCESS")
    print("Report generation: SUCCESS")

    print("\nCleaned dataset:")
    print(CLEANED_DATA_PATH)

    print("\nVisualization directory:")
    print(VISUALIZATION_DIR)

    print("\nReport file:")
    print(REPORT_PATH)

    print(
        "\nCOMPLETE DATA ANALYSIS PIPELINE "
        "EXECUTED SUCCESSFULLY."
    )

    return cleaned_df, results


# ============================================================
# 11. PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    try:

        main()

    except (
        ValueError,
        RuntimeError,
        OSError,
        KeyError
    ) as error:

        plt.close("all")

        print("\nPROJECT EXECUTION FAILED:")
        print(error)

        sys.exit(1)