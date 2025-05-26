DROP TABLE IF EXISTS cust_level_features;
CREATE TABLE cust_level_features AS
SELECT 
    customer_id,
    COUNT(o.order_id) AS num_orders,
    ROUND(SUM(oi.price), 1) AS total_order_value,
    ROUND(SUM(oi.price), 1) / COUNT(o.order_id) AS avg_order_value,
    COUNT(oi.order_item_id) * 1.0 / COUNT(DISTINCT o.order_id) AS avg_items_per_order,
    AVG(DATE(o.order_delivered_customer_date) - DATE(o.order_purchase_timestamp)) AS avg_delivery_time_days,
    AVG(r.review_score) as avg_review_score
FROM 
    orders_data o
JOIN   
    order_items_data oi ON o.order_id = oi.order_id
JOIN
    order_reviews_data r ON o.order_id = r.order_id
GROUP BY 
    o.customer_id

    