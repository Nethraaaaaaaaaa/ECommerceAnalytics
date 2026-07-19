-- ==========================================
-- AGGREGATION & JOIN QUERIES
-- ==========================================

--------------------------------------------------
-- 1. Total Number of Customers
--------------------------------------------------

SELECT COUNT(*) AS total_customers
FROM customers;


--------------------------------------------------
-- 2. Total Number of Products
--------------------------------------------------

SELECT COUNT(*) AS total_products
FROM products;


--------------------------------------------------
-- 3. Total Number of Orders
--------------------------------------------------

SELECT COUNT(*) AS total_orders
FROM orders;


--------------------------------------------------
-- 4. Orders by Status
--------------------------------------------------

SELECT
    status,
    COUNT(*) AS total_orders
FROM orders
GROUP BY status
ORDER BY total_orders DESC;


--------------------------------------------------
-- 5. Customers by Type
--------------------------------------------------

SELECT
    customer_type,
    COUNT(*) AS total_customers
FROM customers
GROUP BY customer_type
ORDER BY total_customers DESC;


--------------------------------------------------
-- 6. Products in Each Category
--------------------------------------------------

SELECT
    category,
    COUNT(*) AS total_products
FROM products
GROUP BY category
ORDER BY total_products DESC;


--------------------------------------------------
-- 7. Products in Each Subcategory
--------------------------------------------------

SELECT
    subcategory,
    COUNT(*) AS total_products
FROM products
GROUP BY subcategory
ORDER BY total_products DESC;


--------------------------------------------------
-- 8. Total Sales by Customer
--------------------------------------------------

SELECT
    c.customer_id,
    c.customer_name,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_sales
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY
    c.customer_id,
    c.customer_name
ORDER BY total_sales DESC;


--------------------------------------------------
-- 9. Top 10 Customers by Sales
--------------------------------------------------

SELECT
    c.customer_id,
    c.customer_name,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_sales
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY
    c.customer_id,
    c.customer_name
ORDER BY total_sales DESC
LIMIT 10;


--------------------------------------------------
-- 10. Revenue by Category
--------------------------------------------------

SELECT
    p.category,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS revenue
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY revenue DESC;


--------------------------------------------------
-- 11. Revenue by Region
--------------------------------------------------

SELECT
    o.region_code,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS revenue
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY o.region_code
ORDER BY revenue DESC;


--------------------------------------------------
-- 12. Average Order Value
--------------------------------------------------

SELECT
    ROUND(AVG(order_total), 2) AS average_order_value
FROM
(
    SELECT
        order_id,
        SUM(quantity * unit_price) AS order_total
    FROM order_items
    GROUP BY order_id
);


--------------------------------------------------
-- 13. Top 10 Most Sold Products
--------------------------------------------------

SELECT
    p.product_name,
    SUM(oi.quantity) AS total_quantity
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY total_quantity DESC
LIMIT 10;


--------------------------------------------------
-- 14. Orders per Customer
--------------------------------------------------

SELECT
    c.customer_name,
    COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_name
ORDER BY total_orders DESC;


--------------------------------------------------
-- 15. Customers with More Than 5 Orders
--------------------------------------------------

SELECT
    c.customer_id,
    c.customer_name,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.customer_name
HAVING COUNT(o.order_id) > 5
ORDER BY total_orders DESC;