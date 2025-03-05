import pandas as pd
import numpy as np

# Load order data from CSV
orders_df = pd.read_csv("order.csv")

# Generating random ratings (1 to 5) for each order
orders_df["rating"] = np.random.randint(1, 6, size=len(orders_df))

# Selecting the required columns for the rating table
rating_table = orders_df[["orderId", "user_id", "restaurant_id", "rating"]]

# Renaming columns to match the required format
rating_table.columns = ["order_id", "user_id", "restaurant_id", "rating"]

# Save the rating table to a new CSV file
rating_table.to_csv("rating_table.csv", index=False)

# Display the final rating table
print(rating_table)
