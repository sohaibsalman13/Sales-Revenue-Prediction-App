DROP TABLE IF EXISTS product_level_features;
CREATE TABLE product_level_featurs AS
SELECT
    product_id,
    product_category_name,
    product_length_cm * product_height_cm * product_width_cm AS product_volume_cm,
    product_photos_qty AS num_of_images
FROM
    products_data