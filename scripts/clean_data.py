import os
import re
import pandas as pd

# =====================================================
# Folder Paths
# =====================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
CLEAN_DIR = os.path.join(BASE_DIR, "data", "cleaned")

os.makedirs(CLEAN_DIR, exist_ok=True)

# =====================================================
# Load Raw Data
# =====================================================

customers = pd.read_csv(
    os.path.join(RAW_DIR, "customers.csv")
)

products = pd.read_csv(
    os.path.join(RAW_DIR, "products.csv")
)

orders = pd.read_csv(
    os.path.join(RAW_DIR, "orders.csv")
)

order_items = pd.read_csv(
    os.path.join(RAW_DIR, "order_items.csv")
)

# =====================================================
# Clean Customers
# =====================================================

def clean_customers(df):

    df = df.copy()

    df = df.drop_duplicates()

    df["customer_name"] = (
        df["customer_name"]
        .str.strip()
    )

    df["customer_type"] = (
        df["customer_type"]
        .str.upper()
    )

    return df


# =====================================================
# Clean Products
# =====================================================

def clean_products(df):

    df = df.copy()

    df = df.drop_duplicates()

    df["product_name"] = (
        df["product_name"]
        .str.strip()
        .str.title()
    )

    return df


# =====================================================
# Clean Orders
# =====================================================

def clean_orders(df):

    df = df.copy()

    df = df.drop_duplicates()

    df["customer_id"] = df["customer_id"].fillna(
        "UNKNOWN"
    )

    df["order_date"] = pd.to_datetime(
    df["order_date"],
    errors="coerce"
)

    return df


# =====================================================
# Validate Emails
# =====================================================

def validate_emails(df):

    email_pattern = (
        r'^[A-Za-z0-9._%+-]+'
        r'@[A-Za-z0-9.-]+'
        r'\.[A-Za-z]{2,}$'
    )

    invalid_emails = df[
        ~df["email"].str.match(
            email_pattern,
            na=False
        )
    ]

    return invalid_emails


# =====================================================
# Check Referential Integrity
# =====================================================

def check_referential_integrity(
    orders_df,
    order_items_df
):

    invalid_items = order_items_df[
        ~order_items_df["order_id"].isin(
            orders_df["order_id"]
        )
    ]

    return invalid_items


# =====================================================
# Clean Order Items
# =====================================================

def clean_order_items(df):

    df = df.copy()

    df = df.drop_duplicates()

    df = df[
        df["quantity"] != 0
    ]

    return df
# =====================================================
# Main Function
# =====================================================

def main():

    print("Cleaning Customers...")
    customers_clean = clean_customers(customers)

    print("Cleaning Products...")
    products_clean = clean_products(products)

    print("Cleaning Orders...")
    orders_clean = clean_orders(orders)

    # Remove orders whose customer_id doesn't exist
    orders_clean = orders_clean[
        orders_clean["customer_id"].isin(
            customers_clean["customer_id"]
        )
    ]

    print("Cleaning Order Items...")
    order_items_clean = clean_order_items(order_items)

    # Remove order_items with invalid order_id
    order_items_clean = order_items_clean[
        order_items_clean["order_id"].isin(
            orders_clean["order_id"]
        )
    ]

    print("Checking Invalid Emails...")
    invalid_emails = validate_emails(customers)

    print("Checking Referential Integrity...")
    invalid_order_items = check_referential_integrity(
        orders,
        order_items
    )

    # =================================================
    # Save Cleaned Files
    # =================================================

    customers_clean.to_csv(
        os.path.join(CLEAN_DIR, "customers_clean.csv"),
        index=False
    )

    products_clean.to_csv(
        os.path.join(CLEAN_DIR, "products_clean.csv"),
        index=False
    )

    orders_clean.to_csv(
        os.path.join(CLEAN_DIR, "orders_clean.csv"),
        index=False
    )

    order_items_clean.to_csv(
        os.path.join(CLEAN_DIR, "order_items_clean.csv"),
        index=False
    )

    invalid_emails.to_csv(
        os.path.join(CLEAN_DIR, "invalid_emails.csv"),
        index=False
    )

    invalid_order_items.to_csv(
        os.path.join(
            CLEAN_DIR,
            "invalid_order_items.csv"
        ),
        index=False
    )

    # =================================================
    # Issues Report
    # =================================================

    with open(
        os.path.join(CLEAN_DIR, "issues_report.txt"),
        "w"
    ) as report:

        report.write("E-Commerce Data Cleaning Report\n")
        report.write("=" * 40 + "\n\n")

        report.write(
            f"Customers : {len(customers_clean)}\n"
        )

        report.write(
            f"Products : {len(products_clean)}\n"
        )

        report.write(
            f"Orders : {len(orders_clean)}\n"
        )

        report.write(
            f"Order Items : {len(order_items_clean)}\n\n"
        )

        report.write(
            f"Invalid Emails : {len(invalid_emails)}\n"
        )

        report.write(
            f"Invalid Order References : {len(invalid_order_items)}\n"
        )

    print("\n====================================")
    print("Data Cleaning Completed Successfully")
    print("====================================")

    print(f"\nFiles saved in:\n{CLEAN_DIR}")


if __name__ == "__main__":
    main()