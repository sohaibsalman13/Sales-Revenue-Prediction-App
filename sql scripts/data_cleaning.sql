-- removing rows where column values are null
-- repeat for all columns of each table

DELETE FROM products_data
WHERE product_id IS NULL
OR product_category_name IS NULL
OR product_name_lenght IS NULL
OR product_description_lenght IS NULL
OR product_photos_qty IS NULL
OR product_weight_g IS NULL
OR product_length_cm IS NULL
OR product_height_cm IS NULL
OR product_width_cm IS NULL;

-- checking the number of null values in each column
-- repeat for all columns of each table

SELECT 
    COUNT(*) - COUNT(order_id) as col1,
    COUNT(*) - COUNT(customer_id) as col2,
    COUNT(*) - COUNT(order_status) as col3,
    COUNT(*) - COUNT(order_purchase_timestamp) as col4,
    COUNT(*) - COUNT(order_approved_at) as col5,
    COUNT(*) - COUNT(order_delivered_carrier_date) as col6,
    COUNT(*) - COUNT(order_delivered_customer_date) as col7,
    COUNT(*) - COUNT(order_estimated_delivery_date) as col1
FROM orders_data