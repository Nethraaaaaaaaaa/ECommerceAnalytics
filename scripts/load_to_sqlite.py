import os
import sqlite3
import pandas as pd

# =====================================================
# Project Paths
# =====================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = os.path.join(
    BASE_DIR,
    "database",
    "ecommerce.db"
)

CLEAN_DIR = os.path.join(
    BASE_DIR,
    "data",
    "cleaned"
)

# =====================================================
# Connect to SQLite
# =====================================================

conn = sqlite3.connect(DB_PATH)

print("Connected to SQLite Database.")

# =====================================================
# Read Cleaned CSV Files
# =====================================================

customers = pd.read_csv(
    os.path.join(
        CLEAN_DIR,
        "customers_clean.csv"
    )
)

products = pd.read_csv(
    os.path.join(
        CLEAN_DIR,
        "products_clean.csv"
    )
)

orders = pd.read_csv(
    os.path.join(
        CLEAN_DIR,
        "orders_clean.csv"
    )
)

order_items = pd.read_csv(
    os.path.join(
        CLEAN_DIR,
        "order_items_clean.csv"
    )
)

print("CSV files loaded successfully.")

# =====================================================
# Clear Existing Data
# =====================================================

cursor = conn.cursor()

cursor.execute("DELETE FROM order_items")
cursor.execute("DELETE FROM orders")
cursor.execute("DELETE FROM products")
cursor.execute("DELETE FROM customers")

conn.commit()

print("Existing records deleted.")
# =====================================================
# Load Data into SQLite Tables
# =====================================================

customers.to_sql(
    "customers",
    conn,
    if_exists="append",
    index=False
)

print("Customers loaded successfully.")

products.to_sql(
    "products",
    conn,
    if_exists="append",
    index=False
)

print("Products loaded successfully.")

orders.to_sql(
    "orders",
    conn,
    if_exists="append",
    index=False
)

print("Orders loaded successfully.")

order_items.to_sql(
    "order_items",
    conn,
    if_exists="append",
    index=False
)

print("Order Items loaded successfully.")

# =====================================================
# Verify Record Counts
# =====================================================

tables = [
    "customers",
    "products",
    "orders",
    "order_items"
]

print("\n========== Record Count ==========")

for table in tables:
    count = pd.read_sql_query(
        f"SELECT COUNT(*) AS total FROM {table}",
        conn
    )
    print(f"{table}: {count['total'][0]} records")

# =====================================================
# Close Connection
# =====================================================

conn.commit()
conn.close()

print("\n===================================")
print("Data Loaded Successfully!")
print("Database Updated.")
print("===================================")