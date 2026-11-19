# Week 7: Statistical Business Analysis

## 1. Project Overview

This project focuses on applying statistical techniques to analyze business sales data and generate meaningful business insights.

Using Python and statistical analysis libraries, the project explores sales patterns, data distributions, relationships between business metrics, hypothesis testing, confidence intervals, and regression modelling.

The objective is to understand business performance through statistical methods and translate analytical findings into actionable business recommendations.

## 2. Project Objectives

- Calculate descriptive statistics.
- Analyze probability distributions.
- Perform hypothesis testing.
- Analyze correlations between business metrics.
- Calculate 95% confidence intervals.
- Implement multiple linear regression.
- Evaluate regression model performance.
- Generate actionable business recommendations.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| SciPy | Statistical testing |
| Statsmodels | Statistical analysis |
| Scikit-learn | Regression modelling |
| Jupyter Notebook | Interactive analysis |

## 4. Dataset Description

The project uses a business sales dataset containing the following columns:

- `Date`
- `Product`
- `Quantity`
- `Price`
- `Customer_ID`
- `Region`
- `Total_Sales`

The dataset is used to analyze sales performance across different products and regions.

## 5. Project Structure

```text
week-7-statistical-business-analysis/
│
├── statistical_analysis.ipynb
├── business_data.csv
├── sales_data.csv
├── customer_churn.csv
├── statistical_report.pdf
├── requirements.txt
├── hypothesis_tests_results.txt
├── confidence_intervals.csv
├── regression_results.csv
├── regional_sales_analysis.csv
├── product_sales_analysis.csv
├── README.md
│
└── screenshots/
    ├── Screenshot (456).png
    ├── Screenshot (457).png
    ├── ...
    └── Screenshot (490).png
```

## 6. Project Files Description

| File | Description |
|---|---|
| `statistical_analysis.ipynb` | Main notebook containing the seven days of statistical analysis, calculations, and visualizations. |
| `business_data.csv` | Main dataset used for the analysis. |
| `sales_data.csv` | Original sales dataset. |
| `customer_churn.csv` | Additional supplied dataset. |
| `statistical_report.pdf` | Report summarizing the statistical findings. |
| `requirements.txt` | List of required Python libraries. |
| `hypothesis_tests_results.txt` | Results of the hypothesis tests. |
| `confidence_intervals.csv` | Calculated confidence intervals. |
| `regression_results.csv` | Regression model results. |
| `regional_sales_analysis.csv` | Regional sales summaries. |
| `product_sales_analysis.csv` | Product performance summaries. |
| `screenshots/` | Screenshots documenting the analysis and visualizations. |

## 7. Statistical Analysis

### Day 1: Descriptive Statistics

Calculated the following descriptive statistics:

- Mean
- Median
- Mode
- Variance
- Standard deviation
- Minimum and maximum values
- Quartiles

The Pandas `describe()` function was also used to generate a statistical summary of numerical columns.

### Day 2: Data Distribution Analysis

Analyzed the distribution of business sales data using:

- Histograms
- Kernel Density Estimation (KDE)
- Box plots
- Shapiro-Wilk normality test

These visualizations and statistical tests helped examine the distribution, spread, and potential outliers in the sales data.

### Day 3: Correlation Analysis

Performed Pearson correlation analysis to examine relationships between:

- Quantity and Total_Sales
- Price and Total_Sales

Created a correlation matrix and heatmap using Seaborn.

Scatter plots were also generated to visualize relationships between numerical variables.

### Day 4: Hypothesis Testing

Performed three hypothesis tests:

**1. Welch's Independent Samples T-Test**

Compared average sales between two regions to determine whether their mean sales differed significantly.

**2. One-Way ANOVA – Region**

Tested whether average sales differed significantly across different regions.

**3. One-Way ANOVA – Product**

Tested whether average sales differed significantly across different products.

The p-values were used to evaluate the null hypotheses at a 5% significance level.

### Day 5: Confidence Intervals

Calculated 95% confidence intervals for:

- Quantity
- Price
- Total_Sales

Also calculated the margin of error and visualized the confidence intervals using error-bar plots.

### Day 6: Regression Analysis

Implemented Multiple Linear Regression using:

- **Independent variables:** Quantity and Price
- **Dependent variable:** Total_Sales

The dataset was divided into training and testing sets using an 80:20 split.

Model performance was evaluated using:

- R-squared
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

**Model Performance**

| Metric | Result |
|---|---:|
| R-squared | 0.863 |
| MAE | 29,724.69 |
| RMSE | 38,244.39 |

**Regression Limitation**

Total_Sales is calculated using Quantity multiplied by Price. Therefore, the regression model primarily reconstructs this mathematical relationship. Its performance should not be interpreted as evidence of independent causal effects.

### Day 7: Business Insights

Performed business analysis to understand sales performance across products and regions.

The analysis included:

- Total sales by region.
- Average sales by region.
- Total sales by product.
- Average sales by product.
- Identification of the highest-revenue region.
- Identification of the highest-revenue product.

Visualizations were created to compare regional and product performance.

## 8. Business Recommendations

Based on the regional and product sales analysis, the following recommendations can be considered:

1. Prioritize products that generate higher total revenue.
2. Investigate lower-performing products to identify opportunities for improvement.
3. Analyze regional sales performance to identify areas with growth potential.
4. Use average transaction values alongside total revenue when evaluating business performance.
5. Conduct further analysis using additional business variables to understand factors influencing sales.

These recommendations should be interpreted alongside the actual findings presented in the notebook and statistical report.

## 9. Screenshots

Screenshots documenting the statistical analysis and visualizations are available in the `screenshots/` directory.

The screenshots cover:

1. Descriptive statistics.
2. Distribution analysis.
3. Correlation heatmap.
4. Hypothesis testing results.
5. Confidence interval visualization.
6. Regression analysis.
7. Business insights.

## 10. How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/Sankarshancn-lab/developers-arena-python-tasks.git
```

### Step 2: Navigate to the Project Directory

```bash
cd developers-arena-python-tasks/week-7-statistical-business-analysis
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Environment

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Launch Jupyter Notebook

```bash
jupyter notebook
```

Open `statistical_analysis.ipynb` and execute all cells sequentially.

## 11. Limitations

- The supplied dataset does not contain marketing expenditure. Therefore, marketing spend versus revenue analysis could not be performed.
- The regression model uses Quantity and Price to predict Total_Sales, which is derived from those variables.
- Regression results should not be interpreted as independent causal effects.
- Business recommendations are based on the available dataset and may require additional information for further validation.

## 12. Conclusion

This project demonstrates the practical application of statistical methods in business data analysis.

The seven-day workflow covered descriptive statistics, distribution analysis, correlation, hypothesis testing, confidence intervals, regression analysis, and business insights.

The project provided practical experience in Python-based statistical analysis, data visualization, model evaluation, and translating analytical findings into business recommendations.

## 13. Author

**Sankarshan CN**

M.Tech – Data Science

GitHub: https://github.com/Sankarshancn-lab