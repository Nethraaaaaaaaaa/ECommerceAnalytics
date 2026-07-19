import os
import random
from datetime import datetime, timedelta

import pandas as pd
from faker import Faker

# -----------------------------
# Configuration
# -----------------------------

fake = Faker()
random.seed(42)
Faker.seed(42)

NUM_CUSTOMERS = 600
NUM_PRODUCTS = 500
NUM_ORDERS = 1200
NUM_ORDER_ITEMS = 3000

customer_types = [
    "REGULAR",
    "PREMIUM",
    "VIP"
]

order_status = [
    "PLACED",
    "SHIPPED",
    "DELIVERED",
    "CANCELLED",
    "RETURNED"
]

regions = [
    "NORTH",
    "SOUTH",
    "EAST",
    "WEST"
]

categories = {
    "Electronics": ["Mobile", "Laptop", "Headphones", "Television"],
    "Clothing": ["Men", "Women", "Kids"],
    "Home": ["Furniture", "Kitchen", "Decor"],
    "Books": ["Education", "Novel", "Comics"],
    "Beauty": ["Skincare", "Makeup"]
}

# -----------------------------
# Folder Paths
# -----------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "data", "raw")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------
# Generate Customers
# -----------------------------

def generate_customers():
    customers = []

    for i in range(1, NUM_CUSTOMERS + 1):

        customer_id = f"CUST{i:04d}"
        customer_name = fake.name()

        email = fake.email()

        # 2% invalid emails
        if random.random() < 0.02:
            invalid_type = random.choice([1, 2])

            if invalid_type == 1:
                email = email.replace("@", "")
            else:
                email = email.split("@")[0] + "@"

        registration_date = fake.date_between(
            start_date="-3y",
            end_date="today"
        )

        customer_type = random.choice(customer_types)

        customers.append({
            "customer_id": customer_id,
            "customer_name": customer_name,
            "email": email,
            "registration_date": registration_date,
            "customer_type": customer_type
        })

    customers_df = pd.DataFrame(customers)

    customers_df.to_csv(
        os.path.join(OUTPUT_DIR, "customers.csv"),
        index=False
    )

    print("customers.csv generated successfully!")

    return customers_df
# -----------------------------
# Generate Products
# -----------------------------

def generate_products():

    products = []

    product_names = {

        "Electronics": [
            "iPhone 15", "Samsung Galaxy", "Dell Laptop",
            "Sony Headphones", "LG Smart TV", "Canon Camera",
            "Apple Watch", "Bluetooth Speaker",
            "Gaming Mouse", "Mechanical Keyboard"
        ],

        "Clothing": [
            "Men T-Shirt", "Women Kurti", "Jeans",
            "Jacket", "Sweater", "Formal Shirt",
            "Hoodie", "Track Pants",
            "Saree", "Kids Dress"
        ],

        "Home": [
            "Dining Table", "Sofa", "Office Chair",
            "Bed", "Cookware Set", "Wall Clock",
            "Curtains", "Bookshelf",
            "Lamp", "Cupboard"
        ],

        "Books": [
            "Python Programming",
            "SQL Basics",
            "Data Science",
            "Machine Learning",
            "Algorithms",
            "Operating Systems",
            "Java Programming",
            "Cloud Computing",
            "AI Handbook",
            "Database Systems"
        ],

        "Beauty": [
            "Face Wash",
            "Lipstick",
            "Perfume",
            "Shampoo",
            "Conditioner",
            "Body Lotion",
            "Face Cream",
            "Sunscreen",
            "Hair Oil",
            "Makeup Kit"
        ]

    }

    for i in range(1, NUM_PRODUCTS + 1):

        product_id = f"PROD{i:04d}"

        category = random.choice(list(categories.keys()))

        subcategory = random.choice(categories[category])

        product_name = random.choice(product_names[category])

        chance = random.random()

        if chance < 0.03:
            product_name = "  " + product_name + "  "

        elif chance < 0.06:
            product_name = product_name.swapcase()

        cost_price = round(
            random.uniform(100, 50000),
            2
        )

        products.append({

            "product_id": product_id,
            "product_name": product_name,
            "category": category,
            "subcategory": subcategory,
            "cost_price": cost_price

        })

    products_df = pd.DataFrame(products)

    products_df.to_csv(
        os.path.join(OUTPUT_DIR, "products.csv"),
        index=False
    )

    print("products.csv generated successfully!")

    return products_df
# -----------------------------
# Generate Orders
# -----------------------------

def generate_orders():

    orders = []

    customer_ids = customers_df["customer_id"].tolist()

    for i in range(1, NUM_ORDERS + 1):

        order_id = f"ORD{i:06d}"

        # 5% NULL customer IDs
        if random.random() < 0.05:
            customer_id = None
        else:
            customer_id = random.choice(customer_ids)

        order_date = fake.date_time_between(
            start_date="-2y",
            end_date="now"
        )

        # 3% incorrect date format
        if random.random() < 0.03:
            order_date = order_date.strftime("%d-%m-%Y")
        else:
            order_date = order_date.strftime("%Y-%m-%d %H:%M:%S")

        status = random.choice(order_status)

        region_code = random.choice(regions)

        orders.append({
            "order_id": order_id,
            "customer_id": customer_id,
            "order_date": order_date,
            "status": status,
            "region_code": region_code
        })

    orders_df = pd.DataFrame(orders)

    orders_df.to_csv(
        os.path.join(OUTPUT_DIR, "orders.csv"),
        index=False
    )

    print("orders.csv generated successfully!")

    return orders_df
# -----------------------------
# Generate Order Items
# -----------------------------

def generate_order_items():

    order_items = []

    order_ids = orders_df["order_id"].tolist()

    product_ids = products_df["product_id"].tolist()

    product_price = dict(
        zip(
            products_df["product_id"],
            products_df["cost_price"]
        )
    )

    for i in range(1, NUM_ORDER_ITEMS + 1):

        item_id = f"ITEM{i:06d}"

        # 2% invalid order IDs
        if random.random() < 0.02:
            order_id = "ORD999999"
        else:
            order_id = random.choice(order_ids)

        product_id = random.choice(product_ids)

        quantity = random.randint(1, 5)

        # 3% negative quantities
        if random.random() < 0.03:
            quantity = -quantity

        cost_price = product_price[product_id]

        unit_price = round(
            cost_price * random.uniform(1.10, 1.50),
            2
        )

        discount_percent = random.randint(0, 50)

        order_items.append({
            "item_id": item_id,
            "order_id": order_id,
            "product_id": product_id,
            "quantity": quantity,
            "unit_price": unit_price,
            "discount_percent": discount_percent
        })

    order_items_df = pd.DataFrame(order_items)

    order_items_df.to_csv(
        os.path.join(OUTPUT_DIR, "order_items.csv"),
        index=False
    )

    print("order_items.csv generated successfully!")

    return order_items_df
# -----------------------------
# Main Function
# -----------------------------

def main():

    global customers_df
    global products_df
    global orders_df

    customers_df = generate_customers()

    products_df = generate_products()

    orders_df = generate_orders()

    generate_order_items()

    print("\n===================================")
    print("All datasets generated successfully!")
    print(f"Location: {OUTPUT_DIR}")
    print("===================================")


if __name__ == "__main__":
    main()