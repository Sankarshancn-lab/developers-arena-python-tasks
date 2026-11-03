# Customer Sales Analysis & Business Intelligence

## Project Overview

This project focuses on analyzing customer purchasing patterns, sales performance, regional revenue distribution, and product performance using Python and Pandas.

The objective is to transform raw sales data into meaningful business insights through data cleaning, advanced data manipulation, statistical analysis, and professional visualizations.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook
* ReportLab

## Project Structure

```text
Week-5/
│
├── customer_analysis.ipynb
├── sales_data.csv
├── customer_churn.csv
├── cleaned_sales_data.csv
│
├── customer_analysis_results.csv
├── customer_product_affinity.csv
├── customer_retention_analysis.csv
├── monthly_sales_analysis.csv
├── product_sales_analysis.csv
├── regional_sales_analysis.csv
│
├── monthly_revenue_trend.png
├── regional_sales_performance.png
├── top_10_customers.png
├── product_revenue_distribution.png
├── customer_segmentation.png
│
├── analysis_report.pdf
├── requirements.txt
└── README.md
```

## Key Features

### 1. Data Exploration

* Dataset inspection
* Statistical summaries
* Missing value analysis
* Duplicate detection

### 2. Data Cleaning

* Datetime conversion
* Text standardization
* Missing value handling
* Feature engineering
* Data validation

### 3. Customer Analysis

* Customer spending analysis
* Top 10 customer identification
* Historical customer value
* Purchase frequency
* Customer segmentation

### 4. Sales Analysis

* Monthly revenue aggregation
* Product performance analysis
* Regional sales comparison
* Month-over-month revenue trends

### 5. Advanced Pandas Operations

* GroupBy and aggregation
* Multiple-condition filtering
* Data merging and joining
* Pivot tables
* Customer-product affinity analysis
* Repeat-purchase analysis

### 6. Visualizations

* Monthly revenue trend
* Regional sales performance
* Top 10 customers
* Product revenue distribution
* Customer segmentation

## Important Data Limitations

* The sales and customer churn datasets contain incompatible customer identifiers. Therefore, a direct customer-level merge was not performed.
* A regional lookup merge was implemented to demonstrate Pandas merging operations.
* The sales dataset does not contain transaction identifiers, limiting genuine basket-level cross-selling analysis.
* Customer retention analysis measures repeat purchasing within the available dataset rather than cohort-based retention.

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project directory:

```bash
cd Week-5
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open `customer_analysis.ipynb` and execute the cells sequentially.

## Project Deliverables

* Complete Jupyter Notebook
* Cleaned sales dataset
* Customer and sales analysis outputs
* Five visualization outputs
* PDF business analysis report

## Learning Outcomes

* Advanced Pandas data manipulation
* Data cleaning and preprocessing
* Customer purchasing behaviour analysis
* Business intelligence and KPI analysis
* Data visualization
* Business-oriented analytical reporting

## Author

**Sankarshan CN**

M.Tech Data Science Student
