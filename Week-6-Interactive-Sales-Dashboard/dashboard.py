import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Interactive Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# Change to "₹" if the values in your CSV represent Indian rupees.
CURRENCY_SYMBOL = "$"

# --------------------------------------------------
# 2. DASHBOARD HEADER
# --------------------------------------------------
st.title("📊 Interactive Sales Analytics Dashboard")
st.markdown("### Developers Arena - Sales Performance Analysis")
st.markdown("---")

# --------------------------------------------------
# 3. LOAD DATASET
# --------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/sales_data.csv")
    df.columns = df.columns.str.strip()

    required_columns = [
        "Date", "Product", "Quantity", "Price",
        "Customer_ID", "Region", "Total_Sales"
    ]
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(
            "Missing required columns: " + ", ".join(missing_columns)
        )

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    for column in ["Quantity", "Price", "Total_Sales"]:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    df = df.dropna(subset=required_columns).copy()
    for column in ["Product", "Region", "Customer_ID"]:
        df[column] = df[column].astype(str).str.strip()

    return df


try:
    df = load_data()
except Exception as error:
    st.error(f"Could not load the sales dataset: {error}")
    st.info("Check that data/sales_data.csv exists and has the required columns.")
    st.stop()

if df.empty:
    st.error("The dataset contains no valid records after cleaning.")
    st.stop()

st.success("Sales dataset loaded successfully!")

# --------------------------------------------------
# 4. SIDEBAR FILTERS
# --------------------------------------------------
st.sidebar.header("🔎 Dashboard Filters")

regions = ["All"] + sorted(df["Region"].unique().tolist())
selected_region = st.sidebar.selectbox("Select Region", regions)

products = ["All"] + sorted(df["Product"].unique().tolist())
selected_product = st.sidebar.selectbox("Select Product", products)

min_date = df["Date"].min().date()
max_date = df["Date"].max().date()
selected_dates = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# --------------------------------------------------
# 5. APPLY FILTERS
# --------------------------------------------------
filtered_df = df.copy()

if selected_region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == selected_region]

if selected_product != "All":
    filtered_df = filtered_df[filtered_df["Product"] == selected_product]

if isinstance(selected_dates, (tuple, list)) and len(selected_dates) == 2:
    start_date, end_date = selected_dates
    filtered_df = filtered_df[
        (filtered_df["Date"].dt.date >= start_date)
        & (filtered_df["Date"].dt.date <= end_date)
    ]
elif isinstance(selected_dates, (tuple, list)) and len(selected_dates) == 1:
    chosen_date = selected_dates[0]
    filtered_df = filtered_df[filtered_df["Date"].dt.date == chosen_date]

# --------------------------------------------------
# 6. BUSINESS METRICS
# --------------------------------------------------
total_sales = filtered_df["Total_Sales"].sum()
total_quantity = filtered_df["Quantity"].sum()
total_transactions = len(filtered_df)
total_customers = filtered_df["Customer_ID"].nunique()
average_sales = total_sales / total_transactions if total_transactions else 0

# --------------------------------------------------
# 7. KPI DASHBOARD
# --------------------------------------------------
st.markdown("---")
st.subheader("📈 Key Business Metrics")
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"{CURRENCY_SYMBOL}{total_sales:,.2f}")
col2.metric("Total Quantity Sold", f"{total_quantity:,.0f}")
col3.metric("Total Transactions", f"{total_transactions:,}")
col4.metric("Unique Customers", f"{total_customers:,}")

# --------------------------------------------------
# 8. DATASET OVERVIEW
# --------------------------------------------------
st.markdown("---")
st.subheader("📋 Dataset Overview")
col1, col2, col3 = st.columns(3)

col1.metric("Filtered Records", f"{len(filtered_df):,}")
col2.metric("Average Sales per Record", f"{CURRENCY_SYMBOL}{average_sales:,.2f}")
col3.metric("Products", f"{filtered_df['Product'].nunique():,}")

# --------------------------------------------------
# 9. CHARTS AND TABLES
# --------------------------------------------------
if filtered_df.empty:
    st.warning("No data available for the selected filters.")
else:
    # --------------------------------------------------
    # 10. MONTHLY SALES TREND
    # --------------------------------------------------
    st.markdown("---")
    st.subheader("📈 Monthly Sales Trend")

    monthly_sales = (
        filtered_df.assign(
            Month=filtered_df["Date"].dt.to_period("M").dt.to_timestamp()
        )
        .groupby("Month", as_index=False)["Total_Sales"]
        .sum()
        .sort_values("Month")
    )

    fig_monthly = px.line(
        monthly_sales,
        x="Month",
        y="Total_Sales",
        title="Monthly Sales Performance",
        markers=True,
        template="plotly_dark"
    )
    fig_monthly.update_xaxes(
        tickformat="%b %Y",
        dtick="M1",
        ticklabelmode="period"
    )
    fig_monthly.update_yaxes(
        tickprefix=CURRENCY_SYMBOL,
        separatethousands=True
    )
    fig_monthly.update_layout(
        xaxis_title="Month",
        yaxis_title="Total Sales",
        title_x=0.5,
        hovermode="x unified"
    )
    fig_monthly.update_traces(
        hovertemplate=(
            "%{x|%B %Y}<br>"
            + f"Sales: {CURRENCY_SYMBOL}"
            + "%{y:,.2f}<extra></extra>"
        )
    )
    st.plotly_chart(fig_monthly, use_container_width=True)

    # --------------------------------------------------
    # 11. PRODUCT-WISE SALES
    # --------------------------------------------------
    st.markdown("---")
    st.subheader("🛍️ Product Sales Performance")

    product_sales = (
        filtered_df.groupby("Product", as_index=False)["Total_Sales"]
        .sum()
        .sort_values("Total_Sales", ascending=False)
    )
    fig_product = px.bar(
        product_sales,
        x="Product",
        y="Total_Sales",
        color="Product",
        title="Total Sales by Product",
        text_auto=".2s",
        template="plotly_dark"
    )
    fig_product.update_layout(
        title_x=0.5,
        xaxis_title="Product",
        yaxis_title="Total Sales",
        yaxis_tickprefix=CURRENCY_SYMBOL,
        yaxis_separatethousands=True
    )
    st.plotly_chart(fig_product, use_container_width=True)

    # --------------------------------------------------
    # 12. REGIONAL SALES PERFORMANCE
    # --------------------------------------------------
    st.markdown("---")
    st.subheader("🌎 Regional Sales Performance")

    regional_sales = (
        filtered_df.groupby("Region", as_index=False)["Total_Sales"]
        .sum()
        .sort_values("Total_Sales", ascending=False)
    )
    fig_region = px.bar(
        regional_sales,
        x="Region",
        y="Total_Sales",
        color="Region",
        title="Sales Distribution Across Regions",
        text_auto=".2s",
        template="plotly_dark"
    )
    fig_region.update_layout(
        title_x=0.5,
        xaxis_title="Region",
        yaxis_title="Total Sales",
        yaxis_tickprefix=CURRENCY_SYMBOL,
        yaxis_separatethousands=True
    )
    st.plotly_chart(fig_region, use_container_width=True)

    # --------------------------------------------------
    # 13. QUANTITY ANALYSIS
    # --------------------------------------------------
    st.markdown("---")
    st.subheader("📦 Product Quantity Analysis")

    quantity_data = (
        filtered_df.groupby("Product", as_index=False)["Quantity"]
        .sum()
        .sort_values("Quantity", ascending=False)
    )
    fig_quantity = px.bar(
        quantity_data,
        x="Product",
        y="Quantity",
        color="Product",
        title="Quantity Sold by Product",
        text_auto=True,
        template="plotly_dark"
    )
    fig_quantity.update_layout(
        title_x=0.5,
        xaxis_title="Product",
        yaxis_title="Total Quantity Sold"
    )
    st.plotly_chart(fig_quantity, use_container_width=True)

    # --------------------------------------------------
    # 14. CUSTOMER SALES ANALYSIS
    # --------------------------------------------------
    st.markdown("---")
    st.subheader("👥 Customer Sales Analysis")

    customer_data = (
        filtered_df.groupby("Customer_ID")
        .agg(
            Total_Sales=("Total_Sales", "sum"),
            Total_Quantity=("Quantity", "sum"),
            Transactions=("Product", "count")
        )
        .reset_index()
    )

    # Bubble size now represents customer sales, not transaction count.
    fig_customer = px.scatter(
        customer_data,
        x="Total_Quantity",
        y="Total_Sales",
        size="Total_Sales",
        color="Total_Sales",
        color_continuous_scale="Blues",
        hover_name="Customer_ID",
        hover_data={
            "Total_Sales": ":,.2f",
            "Total_Quantity": True,
            "Transactions": True
        },
        title="Customer Sales vs Quantity Analysis",
        template="plotly_dark",
        size_max=40
    )
    fig_customer.update_layout(
        title_x=0.5,
        xaxis_title="Total Quantity Purchased",
        yaxis_title="Total Customer Sales",
        yaxis_tickprefix=CURRENCY_SYMBOL,
        yaxis_separatethousands=True,
        coloraxis_colorbar_title="Total Sales"
    )
    st.plotly_chart(fig_customer, use_container_width=True)

    # --------------------------------------------------
    # 15. TOP 5 PRODUCTS
    # --------------------------------------------------
    st.markdown("---")
    st.subheader("🏆 Top 5 Products by Sales")

    top_products = product_sales.head(5).merge(
        quantity_data,
        on="Product",
        how="left"
    )
    st.dataframe(
        top_products,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Product": st.column_config.TextColumn("Product"),
            "Total_Sales": st.column_config.NumberColumn(
                "Total Sales",
                format=f"{CURRENCY_SYMBOL}%.2f"
            ),
            "Quantity": st.column_config.NumberColumn(
                "Total Quantity",
                format="%d"
            )
        }
    )

    # --------------------------------------------------
    # 16. CUSTOMER PERFORMANCE TABLE
    # --------------------------------------------------
    st.markdown("---")
    st.subheader("⭐ Top 5 Customers by Sales")

    top_customers = (
        customer_data.sort_values("Total_Sales", ascending=False).head(5)
    )
    st.dataframe(
        top_customers,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Customer_ID": st.column_config.TextColumn("Customer ID"),
            "Total_Sales": st.column_config.NumberColumn(
                "Total Sales",
                format=f"{CURRENCY_SYMBOL}%.2f"
            ),
            "Total_Quantity": st.column_config.NumberColumn(
                "Total Quantity",
                format="%d"
            ),
            "Transactions": st.column_config.NumberColumn(
                "Transactions",
                format="%d"
            )
        }
    )

# --------------------------------------------------
# 17. FOOTER
# --------------------------------------------------
st.markdown("---")
st.caption(
    "Interactive Sales Analytics Dashboard | "
    "Developers Arena – Week 6"
)
