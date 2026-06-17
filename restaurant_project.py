import pandas as pd
import random
from datetime import datetime, timedelta

# Fix seed for database tracking consistency
random.seed(42)

# 1. Structure the Relational Menu Array
menu_items = [
    {"dish_id": 1, "dish_name": "Paneer Butter Masala", "category": "Main Course", "diet": "Vegetarian", "prep_time_min": 15, "cook_time_min": 15, "cost_price_inr": 120, "selling_price_inr": 280, "ingredients_count": 8},
    {"dish_id": 2, "dish_name": "Chicken Tikka Masala", "category": "Main Course", "diet": "Non-Vegetarian", "prep_time_min": 20, "cook_time_min": 20, "cost_price_inr": 160, "selling_price_inr": 340, "ingredients_count": 10},
    {"dish_id": 3, "dish_name": "Dal Makhani", "category": "Main Course", "diet": "Vegetarian", "prep_time_min": 10, "cook_time_min": 40, "cost_price_inr": 80, "selling_price_inr": 220, "ingredients_count": 6},
    {"dish_id": 4, "dish_name": "Veg Biryani", "category": "Main Course", "diet": "Vegetarian", "prep_time_min": 20, "cook_time_min": 25, "cost_price_inr": 90, "selling_price_inr": 240, "ingredients_count": 12},
    {"dish_id": 5, "dish_name": "Chicken Biryani", "category": "Main Course", "diet": "Non-Vegetarian", "prep_time_min": 25, "cook_time_min": 30, "cost_price_inr": 140, "selling_price_inr": 320, "ingredients_count": 14},
    {"dish_id": 6, "dish_name": "Aloo Gobi", "category": "Main Course", "diet": "Vegetarian", "prep_time_min": 10, "cook_time_min": 15, "cost_price_inr": 50, "selling_price_inr": 180, "ingredients_count": 5},
    {"dish_id": 7, "dish_name": "Samosa (2 pcs)", "category": "Snacks", "diet": "Vegetarian", "prep_time_min": 15, "cook_time_min": 10, "cost_price_inr": 20, "selling_price_inr": 60, "ingredients_count": 4},
    {"dish_id": 8, "dish_name": "Garlic Naan", "category": "Breads", "diet": "Vegetarian", "prep_time_min": 5, "cook_time_min": 5, "cost_price_inr": 15, "selling_price_inr": 60, "ingredients_count": 3},
    {"dish_id": 9, "dish_name": "Tandoori Roti", "category": "Breads", "diet": "Vegetarian", "prep_time_min": 3, "cook_time_min": 4, "cost_price_inr": 8, "selling_price_inr": 30, "ingredients_count": 2},
    {"dish_id": 10, "dish_name": "Gulab Jamun (2 pcs)", "category": "Dessert", "diet": "Vegetarian", "prep_time_min": 5, "cook_time_min": 15, "cost_price_inr": 25, "selling_price_inr": 80, "ingredients_count": 4},
    {"dish_id": 11, "dish_name": "Rasmalai (2 pcs)", "category": "Dessert", "diet": "Vegetarian", "prep_time_min": 10, "cook_time_min": 10, "cost_price_inr": 35, "selling_price_inr": 100, "ingredients_count": 5},
    {"dish_id": 12, "dish_name": "Butter Chicken", "category": "Main Course", "diet": "Non-Vegetarian", "prep_time_min": 20, "cook_time_min": 20, "cost_price_inr": 170, "selling_price_inr": 360, "ingredients_count": 9},
    {"dish_id": 13, "dish_name": "Chana Masala", "category": "Main Course", "diet": "Vegetarian", "prep_time_min": 15, "cook_time_min": 20, "cost_price_inr": 60, "selling_price_inr": 190, "ingredients_count": 6},
    {"dish_id": 14, "dish_name": "Palak Paneer", "category": "Main Course", "diet": "Vegetarian", "prep_time_min": 15, "cook_time_min": 15, "cost_price_inr": 110, "selling_price_inr": 270, "ingredients_count": 7},
    {"dish_id": 15, "dish_name": "Masala Dosa", "category": "Main Course", "diet": "Vegetarian", "prep_time_min": 20, "cook_time_min": 10, "cost_price_inr": 40, "selling_price_inr": 140, "ingredients_count": 6}
]

df_menu = pd.DataFrame(menu_items)

# 2. Build Transaction Generators
start_date = datetime(2025, 1, 1)
num_orders = 4500  
orders = []
order_details = []

cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Pune"]
channels = ["Online (Swiggy/Zomato)", "Dine-In", "Takeaway"]

order_detail_id_counter = 1

for order_id in range(1, num_orders + 1):
    random_days = random.randint(0, 365)
    random_hours = random.randint(11, 23) 
    random_minutes = random.randint(0, 59)
    order_time = start_date + timedelta(days=random_days, hours=random_hours, minutes=random_minutes)
    
    orders.append({
        "order_id": order_id,
        "customer_id": random.randint(1001, 1999),
        "order_timestamp": order_time.strftime('%Y-%m-%d %H:%M:%S'),
        "city": random.choice(cities),
        "sales_channel": random.choice(channels)
    })
    
    num_items = random.randint(1, 4)
    chosen_dishes = random.sample(menu_items, num_items)
    
    for dish in chosen_dishes:
        qty = random.randint(1, 3)
        order_details.append({
            "order_detail_id": order_detail_id_counter,
            "order_id": order_id,
            "dish_id": dish["dish_id"],
            "quantity": qty,
            "unit_price_inr": dish["selling_price_inr"],
            "total_price_inr": dish["selling_price_inr"] * qty
        })
        order_detail_id_counter += 1

# Convert lists to structured DataFrames
df_orders = pd.DataFrame(orders)
df_order_details = pd.DataFrame(order_details)

# Export scripts out to your local folder path
df_menu.to_csv("restaurant_menu.csv", index=False)
df_orders.to_csv("restaurant_orders.csv", index=False)
df_order_details.to_csv("restaurant_order_details.csv", index=False)

print("SUCCESS: 3 relational database CSV files saved to your disk folder.")