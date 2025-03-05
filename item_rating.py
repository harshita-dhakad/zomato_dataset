import pandas as pd
import numpy as np

# Load order list data from CSV
order_list_df = pd.read_csv("order_list.csv")

# Generating random item ratings (1 for Like, 0 for Dislike)
order_list_df["rating_item"] = np.random.choice(["Like", "Dislike"], size=len(order_list_df))

# Selecting the required columns for the item rating table
item_rating_table = order_list_df[["item_id", "restaurantId", "user_id", "rating_item"]]

# Renaming columns to match the required format
item_rating_table.columns = ["item_id", "restaurant_id", "user_id", "rating_item"]

# Save the item rating table to a new CSV file
item_rating_table.to_csv("item_rating_table.csv", index=False)

# Display the final item rating table
print(item_rating_table)