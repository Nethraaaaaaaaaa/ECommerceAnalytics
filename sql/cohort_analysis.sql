-- ==========================================
-- CTE & COHORT ANALYSIS QUERIES
-- ==========================================

--------------------------------------------------
-- 1. Customer's First Order Date (CTE)
--------------------------------------------------

WITH first_order AS
(
    SELECT
        customer_id,
        MIN(order_date) AS first_order_date
    FROM orders
    GROUP BY customer_id
)

SELECT
    c.customer_id,
    c.customer_name,
    first_order.first_order_date
FROM customers c
JOIN first_order
ON c.customer_id = first_order.customer_id
ORDER BY first_order.first_order_date;


--------------------------------------------------
-- 2. Monthly New Customers
--------------------------------------------------

WITH first_order AS
(
    SELECT
        customer_id,
        MIN(order_date) AS first_order_date
    FROM orders
    GROUP BY customer_id
)

SELECT
    strftime('%Y-%m', first_order_date) AS cohort_month,
    COUNT(customer_id) AS new_customers
FROM first_order
GROUP BY cohort_month
ORDER BY cohort_month;


--------------------------------------------------
-- 3. Orders by Cohort Month
--------------------------------------------------

WITH first_order AS
(
    SELECT
        customer_id,
        MIN(order_date) AS first_order_date
    FROM orders
    GROUP BY customer_id
)

SELECT
    strftime('%Y-%m', f.first_order_date) AS cohort_month,
    COUNT(o.order_id) AS total_orders
FROM first_order f
JOIN orders o
ON f.customer_id = o.customer_id
GROUP BY cohort_month
ORDER BY cohort_month;


--------------------------------------------------
-- 4. Revenue by Cohort Month
--------------------------------------------------

WITH first_order AS
(
    SELECT
        customer_id,
        MIN(order_date) AS first_order_date
    FROM orders
    GROUP BY customer_id
)

SELECT
    strftime('%Y-%m', f.first_order_date) AS cohort_month,

    ROUND(
        SUM(oi.quantity * oi.unit_price),
        2
    ) AS revenue

FROM first_order f

JOIN orders o
ON f.customer_id = o.customer_id

JOIN order_items oi
ON o.order_id = oi.order_id

GROUP BY cohort_month
ORDER BY cohort_month;


--------------------------------------------------
-- 5. Repeat Customers
--------------------------------------------------

WITH customer_orders AS
(
    SELECT
        customer_id,
        COUNT(order_id) AS total_orders
    FROM orders
    GROUP BY customer_id
)

SELECT
    *
FROM customer_orders
WHERE total_orders > 1
ORDER BY total_orders DESC;


--------------------------------------------------
-- 6. Top 10 Repeat Customers by Revenue
--------------------------------------------------

WITH customer_revenue AS
(
    SELECT
        c.customer_id,
        c.customer_name,

        COUNT(DISTINCT o.order_id) AS total_orders,

        ROUND(
            SUM(oi.quantity * oi.unit_price),
            2
        ) AS revenue

    FROM customers c

    JOIN orders o
    ON c.customer_id = o.customer_id

    JOIN order_items oi
    ON o.order_id = oi.order_id

    GROUP BY
        c.customer_id,
        c.customer_name
)

SELECT *
FROM customer_revenue
WHERE total_orders > 1
ORDER BY revenue DESC
LIMIT 10;


--------------------------------------------------
-- 7. Average Revenue Per Customer
--------------------------------------------------

WITH customer_sales AS
(
    SELECT
        customer_id,

        SUM(quantity * unit_price) AS revenue

    FROM orders o

    JOIN order_items oi
    ON o.order_id = oi.order_id

    GROUP BY customer_id
)

SELECT
    ROUND(
        AVG(revenue),
        2
    ) AS average_customer_revenue
FROM customer_sales;


--------------------------------------------------
-- 8. Customers Without Orders
--------------------------------------------------

SELECT
    c.customer_id,
    c.customer_name
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;


--------------------------------------------------
-- 9. Monthly Revenue Trend
--------------------------------------------------

SELECT

    strftime('%Y-%m', order_date) AS month,

    ROUND(
        SUM(quantity * unit_price),
        2
    ) AS revenue

FROM orders o

JOIN order_items oi
ON o.order_id = oi.order_id

GROUP BY month
ORDER BY month;


--------------------------------------------------
-- 10. Category-wise Revenue
--------------------------------------------------

SELECT

    p.category,

    ROUND(
        SUM(oi.quantity * oi.unit_price),
        2
    ) AS revenue

FROM products p

JOIN order_items oi
ON p.product_id = oi.product_id

GROUP BY p.category
ORDER BY revenue DESC;