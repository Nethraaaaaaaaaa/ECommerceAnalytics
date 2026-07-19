-- ==========================================
-- WINDOW FUNCTION QUERIES
-- ==========================================

--------------------------------------------------
-- 1. Rank Customers by Total Sales
--------------------------------------------------

SELECT
    c.customer_id,
    c.customer_name,
    ROUND(SUM(oi.quantity * oi.unit_price),2) AS total_sales,
    RANK() OVER (
        ORDER BY SUM(oi.quantity * oi.unit_price) DESC
    ) AS sales_rank
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY
    c.customer_id,
    c.customer_name;


--------------------------------------------------
-- 2. Dense Rank Products by Revenue
--------------------------------------------------

SELECT
    p.product_name,
    ROUND(SUM(oi.quantity * oi.unit_price),2) AS revenue,
    DENSE_RANK() OVER(
        ORDER BY SUM(oi.quantity * oi.unit_price) DESC
    ) AS revenue_rank
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.product_name;


--------------------------------------------------
-- 3. Row Number for Orders by Date
--------------------------------------------------

SELECT
    order_id,
    customer_id,
    order_date,
    ROW_NUMBER() OVER(
        ORDER BY order_date
    ) AS row_num
FROM orders;


--------------------------------------------------
-- 4. Running Revenue
--------------------------------------------------

SELECT
    o.order_date,
    SUM(oi.quantity * oi.unit_price) AS daily_sales,

    SUM(
        SUM(oi.quantity * oi.unit_price)
    ) OVER(
        ORDER BY o.order_date
    ) AS running_revenue

FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id

GROUP BY o.order_date
ORDER BY o.order_date;


--------------------------------------------------
-- 5. Customer Purchase Rank within Customer Type
--------------------------------------------------

SELECT
    c.customer_name,
    c.customer_type,

    ROUND(
        SUM(oi.quantity * oi.unit_price),
        2
    ) AS total_sales,

    RANK() OVER(
        PARTITION BY c.customer_type
        ORDER BY SUM(oi.quantity * oi.unit_price) DESC
    ) AS customer_rank

FROM customers c

JOIN orders o
ON c.customer_id = o.customer_id

JOIN order_items oi
ON o.order_id = oi.order_id

GROUP BY
    c.customer_name,
    c.customer_type;


--------------------------------------------------
-- 6. Average Revenue by Category
--------------------------------------------------

SELECT
    p.category,

    ROUND(
        SUM(oi.quantity * oi.unit_price),
        2
    ) AS revenue,

    ROUND(
        AVG(
            SUM(oi.quantity * oi.unit_price)
        ) OVER(),
        2
    ) AS overall_average

FROM products p

JOIN order_items oi
ON p.product_id = oi.product_id

GROUP BY p.category;


--------------------------------------------------
-- 7. Previous Order Date for Each Customer
--------------------------------------------------

SELECT
    customer_id,
    order_id,
    order_date,

    LAG(order_date)
    OVER(
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS previous_order

FROM orders;


--------------------------------------------------
-- 8. Next Order Date for Each Customer
--------------------------------------------------

SELECT
    customer_id,
    order_id,
    order_date,

    LEAD(order_date)
    OVER(
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS next_order

FROM orders;


--------------------------------------------------
-- 9. Highest Revenue Product in Each Category
--------------------------------------------------

SELECT *

FROM
(
    SELECT

        p.category,

        p.product_name,

        ROUND(
            SUM(oi.quantity * oi.unit_price),
            2
        ) AS revenue,

        ROW_NUMBER() OVER(

            PARTITION BY p.category

            ORDER BY
            SUM(oi.quantity * oi.unit_price) DESC

        ) AS rn

    FROM products p

    JOIN order_items oi
    ON p.product_id = oi.product_id

    GROUP BY
        p.category,
        p.product_name

)

WHERE rn = 1;


--------------------------------------------------
-- 10. Running Quantity Sold by Product
--------------------------------------------------

SELECT

    p.product_name,

    o.order_date,

    oi.quantity,

    SUM(oi.quantity)
    OVER(

        PARTITION BY p.product_name

        ORDER BY o.order_date

    ) AS running_quantity

FROM products p

JOIN order_items oi
ON p.product_id = oi.product_id

JOIN orders o
ON oi.order_id = o.order_id;