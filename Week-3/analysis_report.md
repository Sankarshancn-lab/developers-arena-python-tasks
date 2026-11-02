\# Sales Data Analysis Report



\## 1. Project Overview



This project focuses on analyzing retail sales data using Python and the Pandas library.



The objective is to explore sales transactions, clean the dataset, calculate important business metrics, and generate meaningful insights to support business decision-making.



\*\*Internship:\*\* Developers Arena Python Internship

\*\*Project:\*\* Sales Data Analysis

\*\*Technology:\*\* Python, Pandas, CSV



\## 2. Dataset Description



The dataset contains retail sales transactions with the following attributes:



\* Order\_ID

\* Order\_Date

\* Product

\* Category

\* Quantity

\* Unit\_Price

\* Total\_Sales

\* Region



The original dataset contained 13 records and 8 columns.



After data cleaning, 12 valid records were retained.



\## 3. Data Cleaning



The following data-cleaning operations were performed:



\* Identified missing values in Quantity and Region.

\* Filled missing Quantity using the median.

\* Filled missing Region using the mode.

\* Identified and removed duplicate transactions using Order\_ID.

\* Converted Order\_Date into datetime format.

\* Validated numerical values.

\* Recalculated Total\_Sales using Quantity multiplied by Unit\_Price.



\### Cleaning Results



| Metric            | Before Cleaning | After Cleaning |

| ----------------- | --------------: | -------------: |

| Records           |              13 |             12 |

| Missing Quantity  |               1 |              0 |

| Missing Region    |               1 |              0 |

| Duplicate Records |               1 |              0 |

| Columns           |               8 |              8 |



\## 4. Sales Analysis Results



\### Overall Sales Performance



| Metric                    |    Result |

| ------------------------- | --------: |

| Total Revenue             | ₹3,18,300 |

| Total Units Sold          |        38 |

| Average Transaction Value |   ₹26,525 |

| Highest Transaction       | ₹1,10,000 |

| Lowest Transaction        |    ₹2,500 |



\### Product Performance



| Product    | Units Sold |   Revenue |

| ---------- | ---------: | --------: |

| Laptop     |          4 | ₹2,20,000 |

| Mouse      |         15 |    ₹7,500 |

| Keyboard   |          9 |   ₹10,800 |

| Monitor    |          6 |   ₹72,000 |

| Headphones |          4 |    ₹8,000 |



\*\*Best-selling product by quantity:\*\* Mouse



\*\*Highest revenue-generating product:\*\* Laptop



\### Regional Performance



| Region |   Revenue |

| ------ | --------: |

| South  | ₹1,72,200 |

| West   |   ₹72,000 |

| North  |   ₹65,500 |

| East   |    ₹8,600 |



The South region generated the highest revenue.



\### Category Performance



| Category    |   Revenue |

| ----------- | --------: |

| Electronics | ₹2,92,000 |

| Accessories |   ₹26,300 |



Electronics contributed approximately 91.7% of total revenue.



\## 5. Key Business Insights



1\. Laptop generated the highest revenue, contributing approximately 69.1% of total sales.

2\. Mouse recorded the highest sales volume with 15 units sold.

3\. The South region was the strongest-performing region.

4\. Electronics generated the majority of the business revenue.

5\. The average transaction value was ₹26,525.



\## 6. Technologies Used



\* Python: Programming and analysis.

\* Pandas: Data loading, cleaning, manipulation and aggregation.

\* CSV: Dataset storage.

\* Git and GitHub: Version control and project submission.



\## 7. Conclusion



The Sales Data Analysis project successfully demonstrates the use of Python and Pandas for working with real-world datasets.



The project covers data loading, exploration, missing-value handling, duplicate removal, statistical analysis, revenue calculations, and business insight generation.



The analysis identifies important sales trends across products, categories, and regions.



This project demonstrates fundamental data-analysis skills and the ability to convert raw sales data into meaningful business information.



\## 8. Project Status



\*\*Status: Successfully Completed\*\*



All major technical requirements of the Week 3 assignment have been implemented.



