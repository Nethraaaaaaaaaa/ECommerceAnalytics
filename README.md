# 📊 E-Commerce Order Analytics System

An end-to-end data analytics project that simulates a real-world e-commerce workflow using Python, Pandas, SQLite, and SQL. The project generates realistic datasets, performs data cleaning and validation, loads the processed data into a relational database, and generates business insights through SQL queries and a command-line reporting dashboard.

---

## 🚀 Project Overview

Organizations collect large volumes of transactional data every day. Before meaningful business insights can be generated, the data must be cleaned, validated, stored, and analyzed.

This project demonstrates a complete ETL (Extract, Transform, Load) pipeline by:

- Generating realistic e-commerce datasets
- Cleaning and validating raw data
- Loading data into a SQLite database
- Performing SQL-based business analysis
- Building an interactive command-line reporting dashboard

---

# ✨ Features

- Generate realistic e-commerce datasets
- Introduce intentional data inconsistencies
- Clean and validate raw data
- Remove duplicate and invalid records
- Load cleaned data into SQLite
- Execute business analytics using SQL
- Implement Window Functions and CTEs
- Perform Cohort Analysis
- Interactive Command Line Dashboard
- Edge Case Validation Tests

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Data Generation & ETL |
| Pandas | Data Cleaning & Validation |
| Faker | Synthetic Data Generation |
| SQLite | Relational Database |
| SQL | Business Analysis |
| VS Code | Development Environment |

---

# 📁 Project Structure

```
EcommerceAnalytics/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── database/
│   └── ecommerce.db
│
├── output/
│
├── scripts/
│   ├── generate_data.py
│   ├── clean_data.py
│   ├── load_to_sqlite.py
│   ├── report_cli.py
│   └── test_edge_cases.py
│
├── sql/
│   ├── schema.sql
│   ├── aggregation.sql
│   ├── window_functions.sql
│   └── cohort_analysis.sql
│
└── README.md
```

---

# 🔄 ETL Workflow

```
Generate Raw Data
        │
        ▼
Raw CSV Files
        │
        ▼
Data Cleaning & Validation
        │
        ▼
Cleaned CSV Files
        │
        ▼
SQLite Database
        │
        ▼
SQL Analytics
        │
        ▼
CLI Dashboard
```

---

# 📂 Dataset

The project generates four datasets:

### Customers
- Customer ID
- Customer Name
- Email
- Registration Date
- Customer Type

### Products
- Product ID
- Product Name
- Category
- Subcategory
- Cost Price

### Orders
- Order ID
- Customer ID
- Order Date
- Status
- Region Code

### Order Items
- Item ID
- Order ID
- Product ID
- Quantity
- Unit Price
- Discount Percentage

---

# 🧹 Data Cleaning & Validation

The ETL pipeline performs several validation and cleaning operations:

- Remove duplicate records
- Handle missing values
- Standardize text formatting
- Normalize product names
- Validate email addresses
- Fix invalid date formats
- Check referential integrity
- Generate data quality reports

Generated outputs include:

- customers_clean.csv
- products_clean.csv
- orders_clean.csv
- order_items_clean.csv
- invalid_emails.csv
- invalid_order_items.csv
- issues_report.txt

---

# 🗄 Database

The cleaned data is loaded into a SQLite database containing four relational tables:

- Customers
- Products
- Orders
- Order Items

The database uses Primary Keys and Foreign Keys to maintain referential integrity.

---

# 📈 SQL Analysis

The project implements a variety of SQL concepts.

## Aggregations

- COUNT()
- SUM()
- AVG()
- GROUP BY
- HAVING
- ORDER BY

Business Reports:

- Revenue by Category
- Revenue by Region
- Top Customers
- Top Products
- Average Order Value

---

## Window Functions

Implemented:

- ROW_NUMBER()
- RANK()
- DENSE_RANK()
- LAG()
- LEAD()
- PARTITION BY

---

## Common Table Expressions (CTEs)

Used for:

- Monthly Revenue Analysis
- Customer Segmentation
- Repeat Customers
- Revenue Trends
- Cohort Analysis

---

# ⚠️ Edge Case Handling

The project includes validation tests to ensure data quality before analysis.

Implemented checks:

- Invalid order references
- Discount percentage greater than 100
- Zero quantity records
- Future order dates

All validations are implemented in:

```
scripts/test_edge_cases.py
```

---

# 💻 Command Line Dashboard

The application provides a simple command-line interface for analytics.

Available reports include:

- Total Customers
- Total Products
- Total Orders
- Orders by Status
- Top Customers by Sales
- Revenue by Category
- Monthly Revenue

---

# ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/Nethraaaaaaaaaa/EcommerceAnalytics.git
```

Navigate to the project folder:

```bash
cd EcommerceAnalytics
```

Generate datasets:

```bash
python scripts/generate_data.py
```

Clean datasets:

```bash
python scripts/clean_data.py
```

Load data into SQLite:

```bash
python scripts/load_to_sqlite.py
```

Run edge case validation:

```bash
python scripts/test_edge_cases.py
```

Launch the dashboard:

```bash
python scripts/report_cli.py
```

---

# 📊 Skills Demonstrated

- Python Programming
- Data Cleaning
- Data Validation
- ETL Pipeline Development
- Pandas
- SQLite
- SQL
- Aggregation Queries
- Window Functions
- Common Table Expressions (CTEs)
- Cohort Analysis
- Relational Database Design
- Command Line Application Development

---

# 🚀 Future Enhancements

- Interactive Streamlit Dashboard
- Power BI Dashboard
- PostgreSQL/MySQL Support
- Automated ETL Scheduling
- Data Visualization
- Docker Deployment
- Cloud Deployment (AWS/Azure)
