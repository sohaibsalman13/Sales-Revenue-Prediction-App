DROP TABLE IF EXISTS order_level_features;
CREATE TABLE order_level_features AS 
WITH order_features AS (
    SELECT 
        oi.order_id,
        COUNT(oi.order_item_id) AS num_items_per_order,
        ROUND(SUM(oi.price), 1) AS total_price_per_order,
        ROUND((SUM(oi.freight_value) / total_price_per_order), 1) AS freight_ratio,
        COUNT(DISTINCT oi.product_id) AS unique_products_per_order,
        COUNT(DISTINCT oi.seller_id) AS sellers_per_order,
        CASE 
            WHEN COUNT(oi.order_item_id) = 0 THEN NULL
            ELSE ROUND((SUM(oi.price) / COUNT(oi.order_item_id)), 1)
        END AS avg_price_per_item
        

FROM 
    order_items_data oi 
GROUP BY 
    oi.order_id
)

SELECT 
    of.*,
    CASE 
        WHEN o.order_delivered_customer_date IS NULL THEN NULL
        ELSE DATEDIFF(day, o.order_purchase_timestamp, o.order_delivered_customer_date)
    END AS order_duration_days,
    CASE
        WHEN o.order_delivered_customer_date IS NULL 
        OR o.order_estimated_delivery_date IS NULL THEN NULL
        ELSE DATEDIFF(day, o.order_estimated_delivery_date, o.order_delivered_customer_date)
    END AS delayed_delivery_days
FROM 
    order_features of
JOIN 
    orders_data o 
ON 
    of.order_id = o.order_id;