import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = os.path.join(
    BASE_DIR,
    "database",
    "ecommerce.db"
)


def run_query(query):

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


def menu():

    while True:

        print("\n========================================")
        print("   E-Commerce Analytics Dashboard")
        print("========================================")

        print("1. Total Customers")
        print("2. Total Products")
        print("3. Total Orders")
        print("4. Orders by Status")
        print("5. Top 10 Customers by Sales")
        print("6. Revenue by Category")
        print("7. Monthly Revenue")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            query = """
            SELECT COUNT(*) AS total_customers
            FROM customers;
            """

            print(run_query(query))

        elif choice == "2":

            query = """
            SELECT COUNT(*) AS total_products
            FROM products;
            """

            print(run_query(query))

        elif choice == "3":

            query = """
            SELECT COUNT(*) AS total_orders
            FROM orders;
            """

            print(run_query(query))

        elif choice == "4":

            query = """
            SELECT
                status,
                COUNT(*) AS total_orders
            FROM orders
            GROUP BY status;
            """

            print(run_query(query))

        elif choice == "5":

            query = """
            SELECT
                c.customer_name,
                ROUND(
                    SUM(oi.quantity * oi.unit_price),
                    2
                ) AS total_sales

            FROM customers c

            JOIN orders o
            ON c.customer_id = o.customer_id

            JOIN order_items oi
            ON o.order_id = oi.order_id

            GROUP BY
                c.customer_name

            ORDER BY total_sales DESC

            LIMIT 10;
            """

            print(run_query(query))

        elif choice == "6":

            query = """
            SELECT
                p.category,
                ROUND(
                    SUM(
                        oi.quantity * oi.unit_price
                    ),
                    2
                ) AS revenue

            FROM products p

            JOIN order_items oi
            ON p.product_id = oi.product_id

            GROUP BY p.category

            ORDER BY revenue DESC;
            """

            print(run_query(query))

        elif choice == "7":

            query = """
            SELECT

                strftime('%Y-%m', order_date)
                AS month,

                ROUND(
                    SUM(
                        quantity * unit_price
                    ),
                    2
                ) AS revenue

            FROM orders o

            JOIN order_items oi
            ON o.order_id = oi.order_id

            GROUP BY month

            ORDER BY month;
            """

            print(run_query(query))

        elif choice == "8":

            print("\nThank you!")

            break

        else:

            print("\nInvalid Choice")


if __name__ == "__main__":
    menu()