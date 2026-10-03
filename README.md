# 💊 PharmEasy Regional Pulse

### Regional Sales and Business Performance Dashboard

## 📌 Project Overview

PharmEasy Regional Pulse is a data analytics dashboard designed to analyze regional sales, profitability, monthly trends, and product category performance.

The project uses Python, SQL, SQLite, Streamlit, and Plotly to transform order data into meaningful business insights through interactive visualizations.

## 🎯 Project Objectives

* Analyze sales and profit across different regions.
* Track monthly sales and profit trends.
* Compare regional business performance.
* Identify leading product categories.
* Calculate profit margins.
* Generate filtered reports in CSV and Excel formats.

## 🛠️ Technologies Used

* **Python:** Data processing and application logic
* **Pandas:** Data cleaning, transformation, and analysis
* **SQLite:** Database storage and querying
* **SQL:** Data retrieval and aggregation
* **Streamlit:** Interactive dashboard development
* **Plotly:** Interactive charts and visualizations

## 📊 Dashboard Features

* **Business Overview:** Total orders, total sales, total profit, and profit margin.
* **Monthly Sales Trend:** Visualizes sales performance over time.
* **Monthly Profit Analysis:** Tracks monthly profit, sales versus profit, and profit margin.
* **Regional Sales Comparison:** Compares sales performance across regions using a horizontal bar chart.
* **Category Breakdown:** Displays sales contribution by product category.
* **Region and Monthly Details:** Provides detailed regional and monthly performance data.
* **Business Insights:** Highlights regional and category-wise performance.
* **Executive Summary:** Automatically generates key business findings.
* **Interactive Filters:** Filter dashboard results by region and date range.
* **Download Reports:** Export filtered order data and summaries in CSV and Excel formats.

## 📁 Project Structure

```text
pharmeasy-regional-pulse/
│
├── app.py
├── build_db.py
├── queries.py
├── pharmeasy.db
├── pharmeasy_orders_clean.csv
├── pharmeasy_orders_normalized.csv
├── README.md
└── requirements.txt
```

## ⚙️ Installation and Setup

### 1. Clone or download the project

Download the project files and open the project folder in VS Code.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Build the database

```bash
python build_db.py
```

### 4. Run the dashboard

```bash
streamlit run app.py
```

The dashboard will open in your default web browser.

## 📈 Business Value

The dashboard helps users understand regional sales performance, monitor profitability, identify leading product categories, and explore business performance over selected periods.

Its interactive filters and downloadable reports support further analysis and business reporting.

## 👨‍💻 Project

**Project Name:** PharmEasy Regional Pulse
**Domain:** Data Analytics and Business Intelligence
**Application:** Interactive Sales Performance Dashboard
