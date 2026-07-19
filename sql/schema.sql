DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS order_items;

CREATE TABLE customers(
    customer_id TEXT PRIMARY KEY,
    customer_name TEXT,
    email TEXT,
    registration_date TEXT,
    customer_type TEXT
);

CREATE TABLE products(
    product_id TEXT PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    subcategory TEXT,
    cost_price REAL
);

CREATE TABLE orders(
    order_id TEXT PRIMARY KEY,
    customer_id TEXT,
    order_date TEXT,
    status TEXT,
    region_code TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items(
    item_id TEXT PRIMARY KEY,
    order_id TEXT,
    product_id TEXT,
    quantity INTEGER,
    unit_price REAL,
    discount_percent INTEGER,
    FOREIGN KEY(order_id) REFERENCES orders(order_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
);