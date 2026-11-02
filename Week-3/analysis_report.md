\# Sales Data Analysis Report



\## 1. Project Overview



This project performs exploratory data analysis on a sales dataset provided for the Developers Arena Python Internship — Week 3.



The objective is to understand sales performance, identify the best-selling products, compare regional revenue, calculate key business metrics, and generate meaningful insights using Python and Pandas.



\## 2. Dataset Description



The dataset contains 100 sales transactions and 7 columns.



| Column      | Description                    |

| ----------- | ------------------------------ |

| Date        | Date of transaction            |

| Product     | Product purchased              |

| Quantity    | Number of units sold           |

| Price       | Price per unit                 |

| Customer\_ID | Unique customer identifier     |

| Region      | Sales region                   |

| Total\_Sales | Total value of the transaction |



\*\*Dataset period:\*\* 1 January 2024 – 9 April 2024

\*\*Total records:\*\* 100

\*\*Total columns:\*\* 7



\## 3. Data Cleaning and Preprocessing



The following preprocessing operations were performed:



\* Checked the dataset for missing values.

\* Checked for duplicate records.

\* Converted the Date column into datetime format.

\* Verified numeric columns.

\* Checked for invalid or negative quantity and price values.

\* Recalculated Total\_Sales using Quantity × Price.

\* Exported the cleaned dataset to `cleaned\_sales\_data.csv`.



\### Data Quality Results



| Check             | Result |

| ----------------- | -----: |

| Total records     |    100 |

| Missing values    |      0 |

| Duplicate records |      0 |

| Unique customers  |    100 |



The original dataset contained no missing values or duplicate records. Therefore, no missing-value imputation or duplicate removal was necessary.



\## 4. Key Performance Metrics



| Metric                           |      Result |

| -------------------------------- | ----------: |

| Total Revenue                    | ₹12,365,048 |

| Total Units Sold                 |         478 |

| Average Transaction Value        | ₹123,650.48 |

| Average Quantity per Transaction |        4.78 |

| Number of Customers              |         100 |

| Best-Selling Product             |      Laptop |

| Highest Revenue Region           |       North |

| Highest Sales Month              |  March 2024 |



\## 5. Product Performance Analysis



\### Revenue by Product



| Product    |    Revenue |

| ---------- | ---------: |

| Headphones | ₹1,384,033 |

| Laptop     | ₹3,889,210 |

| Monitor    | ₹1,348,071 |

| Phone      | ₹2,859,394 |

| Tablet     | ₹2,884,340 |



\### Quantity Sold by Product



| Product    | Units Sold |

| ---------- | ---------: |

| Laptop     |        136 |

| Tablet     |        127 |

| Phone      |        101 |

| Monitor    |         66 |

| Headphones |         48 |



\*\*Observation:\*\* Laptop was the best-performing product in both total quantity sold and revenue generated.



\## 6. Regional Sales Analysis



| Region |    Revenue |

| ------ | ---------: |

| East   | ₹2,519,639 |

| North  | ₹3,983,635 |

| South  | ₹3,737,852 |

| West   | ₹2,123,922 |



\*\*Observation:\*\* The North region generated the highest revenue, followed by the South region. The West region recorded the lowest revenue.



\## 7. Monthly Sales Analysis



| Month         |    Revenue |

| ------------- | ---------: |

| January 2024  | ₹4,120,524 |

| February 2024 | ₹2,656,050 |

| March 2024    | ₹4,485,006 |

| April 2024    | ₹1,103,468 |



\*\*Observation:\*\* March 2024 recorded the highest revenue.



Note: April contains data only from 1 April to 9 April, so it represents a partial month and should not be directly compared with the complete months.



\## 8. Transaction Analysis



\* Highest transaction value: ₹373,932.

\* Highest transaction date: 16 January 2024.

\* Product in highest transaction: Phone.

\* Lowest transaction value: ₹6,540.

\* Lowest transaction date: 23 February 2024.

\* Product in lowest transaction: Tablet.



\## 9. Conclusion



The analysis identified several useful business insights:



1\. Total sales revenue reached ₹12,365,048 across 100 transactions.

2\. Laptop was the strongest product based on both quantity sold and revenue.

3\. North was the highest-revenue region.

4\. March 2024 recorded the highest monthly revenue.

5\. The dataset contained 100 unique customers and no



