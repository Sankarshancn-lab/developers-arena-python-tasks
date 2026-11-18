\# Interactive Sales Analytics Dashboard



An interactive sales analytics project developed using Python, Pandas, Seaborn, Plotly, and Streamlit. This project analyzes sales transaction data and presents meaningful business insights through statistical analysis, interactive visualizations, and a web-based dashboard.



\## Project Overview



The Interactive Sales Analytics Dashboard helps users explore product performance, regional sales, customer purchasing patterns, and monthly revenue trends.



The project combines exploratory data analysis, statistical visualization, and interactive dashboard development to transform raw sales data into useful business insights.



\## Technologies Used



\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn

\- Plotly

\- Streamlit

\- Jupyter Notebook

\- IPyWidgets



\## Dataset



\*\*Dataset:\*\* Sales Transaction Dataset  

\*\*File:\*\* `data/sales\_data.csv`



The dataset contains 100 sales records and the following columns:



| Column | Description |

|---|---|

| Date | Date of the sales transaction |

| Product | Product purchased |

| Quantity | Quantity sold |

| Price | Unit price |

| Customer\_ID | Unique customer identifier |

| Region | Sales region |

| Total\_Sales | Total transaction sales value |



The dataset covers five products across four regions.



\## Project Features



\### 1. Data Analysis and Visualization



\- Sales distribution analysis

\- Product-wise sales performance

\- Regional sales analysis

\- Sales distribution using boxplots

\- Violin plot analysis

\- Correlation heatmap

\- Statistical analysis using mean, median and standard deviation

\- Outlier detection using the IQR method

\- Monthly sales trend analysis

\- Quantity versus total sales analysis



\### 2. Interactive Visualizations



\- Interactive monthly sales trend

\- Product-wise sales performance

\- Regional sales performance

\- Interactive customer performance analysis

\- Product performance analysis

\- Interactive Plotly charts

\- Interactive product filtering using IPyWidgets



\### 3. Streamlit Dashboard



\- Interactive region filter

\- Product filter

\- Date range filter

\- Key business performance indicators

\- Monthly sales trend visualization

\- Product sales performance chart

\- Regional sales performance chart

\- Product quantity analysis

\- Customer sales analysis

\- Top 5 products by sales

\- Top 5 customers by sales

\- Dynamic dataset overview



\## Key Business Metrics



The dashboard calculates:



\- Total Sales

\- Total Quantity Sold

\- Total Transactions (sales records)

\- Unique Customers

\- Average Sales per Record

\- Number of Products

\- Filtered Records



\## Project Structure



```text

Week-6-Interactive-Sales-Dashboard/

│

├── data/

│   └── sales\_data.csv

│

├── visualizations/

│   ├── Static visualization images

│   └── Interactive HTML charts

│

├── reports/

│

├── dashboard.ipynb

├── dashboard.py

├── dashboard\_demo.gif

├── requirements.txt

├── .gitignore

└── README.md

```



\## Installation and Setup



\### 1. Clone the Repository



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

```



\### 2. Navigate to the Project Directory



```bash

cd Week-6-Interactive-Sales-Dashboard

```



\### 3. Install Dependencies



```bash

pip install -r requirements.txt

```



\### 4. Run the Streamlit Dashboard



```bash

python -m streamlit run dashboard.py

```



\### 5. Open the Application



Open the following address in your browser:



```text

http://localhost:8501

```



\## Key Insights



The analysis provides insights into:



\- Product-wise revenue contribution.

\- Regional sales performance.

\- Monthly revenue fluctuations.

\- Quantity and sales relationships.

\- Highest-performing products.

\- Highest-performing customers.

\- Distribution and variation in transaction values.



\## Learning Outcomes



\- Data cleaning and preprocessing using Pandas.

\- Exploratory Data Analysis.

\- Statistical analysis and outlier detection.

\- Data visualization using Matplotlib and Seaborn.

\- Interactive visualization using Plotly.

\- Interactive widgets using IPyWidgets.

\- Building web-based dashboards using Streamlit.

\- Extracting meaningful business insights from sales data.



\## Project Information



\*\*Program:\*\* Developers Arena – Python Development



\*\*Task:\*\* Week 6 – Data Visualization Mastery



\*\*Project:\*\* Interactive Sales Analytics Dashboard

