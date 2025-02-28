import pandas as pd
import random
from datetime import datetime, timedelta

# Load CSVs using Pandas
userdf = pd.read_csv("./user.csv")
itemdf = pd.read_csv("./item.csv")
resdf = pd.read_csv("./restaurant.csv")

def create_order_item(n):
    order_data = []
    order_ids = set()

    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    total_days = (end_date - start_date).days

    while len(order_ids) < n:
        order_num = random.randint(1, n)
        if order_num in order_ids:
            continue
        order_ids.add(order_num)

        rest_id = random.randint(1, 2000)  # Random restaurant ID
        user_id = random.randint(1, 10000)  # Random user ID
        date = (start_date + timedelta(days=random.randint(0, total_days))).strftime("%Y-%m-%d")

        # Fetch items for the selected restaurant
        restaurant_items = itemdf.query(f"restaurant_id == {rest_id}")[["item_id", "price"]]

        if restaurant_items.empty:
            continue  # Skip if no items exist for the restaurant

        # Select up to `items_per_order` unique items
        items_per_order = min(random.randint(2, 7), len(restaurant_items))
        selected_items = restaurant_items.sample(n=items_per_order, replace=False)

        # Append order details
        for _, row in selected_items.iterrows():
            quantity = random.randint(1, 4)
            order_data.append({
                "orderId": order_num,
                "restaurantId": rest_id,
                "quantity": quantity,
                "item_id": row["item_id"],
                "price": row["price"],
                "total_price": quantity * row["price"],
                "date": date,
                "user_id": user_id
            })

    return order_data

# Generate data
order_data = create_order_item(200000)

# Convert to Pandas DataFrame
df = pd.DataFrame(order_data)

# # Save DataFrame to CSV
df.to_csv("order_list.csv", index=False)

# Display first few rows

