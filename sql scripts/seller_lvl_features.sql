DROP TABLE IF EXISTS seller_level_features;
CREATE TABLE seller_level_features AS
SELECT
    s.seller_id,
    SUM(DISTINCT oi.order_id) AS seller_num_orders,
    ROUND(AVG(oi.freight_value)) AS seller_avg_freight_value
FROM
    sellers_data s
JOIN 
    order_items_data oi ON s.seller_id = oi.seller_id
GROUP BY
    s.seller_id