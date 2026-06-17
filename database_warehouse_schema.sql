-- INDIAN RESTAURANT OPERATIONS DATABASE SCHEMA
CREATE DATABASE IF NOT EXISTS indian_restaurant_db;
USE indian_restaurant_db;

CREATE TABLE restaurant_menu (
    dish_id INT PRIMARY KEY,
    dish_name VARCHAR(100),
    category VARCHAR(50),
    diet VARCHAR(30),
    prep_time_min INT,
    cook_time_min INT,
    cost_price_inr DECIMAL(10,2),
    selling_price_inr DECIMAL(10,2),
    ingredients_count INT
);

CREATE TABLE restaurant_orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_timestamp DATETIME,
    city VARCHAR(50),
    sales_channel VARCHAR(50)
);

CREATE TABLE restaurant_order_details (
    order_detail_id INT PRIMARY KEY,
    order_id INT,
    dish_id INT,
    quantity INT,
    unit_price_inr DECIMAL(10,2),
    total_price_inr DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES restaurant_orders(order_id),
    FOREIGN KEY (dish_id) REFERENCES restaurant_menu(dish_id)
);

-- EXECUTIVE PORTFOLIO VALIDATION QUERY
SELECT 
    m.dish_name,
    m.category,
    SUM(od.quantity) AS total_units_sold,
    SUM(od.total_price_inr) AS total_revenue,
    SUM(od.total_price_inr) - SUM(od.quantity * m.cost_price_inr) AS net_profit
FROM restaurant_order_details od
JOIN restaurant_menu m ON od.dish_id = m.dish_id
GROUP BY m.dish_id, m.dish_name, m.category
ORDER BY net_profit DESC;