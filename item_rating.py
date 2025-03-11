import pandas as pd
import numpy as np

# Load order list data from CSV
order_list_df = pd.read_csv("order_list.csv")

# Generating random item ratings with 70% Like and 30% Dislike
order_list_df["rating_item"] = np.random.choice(["Like", "Dislike"], size=len(order_list_df), p=[0.7, 0.3])

# Selecting the required columns for the item rating table, including order_id
item_rating_table = order_list_df[["orderId", "item_id", "user_id", "date", "rating_item"]]

# Save the item rating table to a new CSV file
item_rating_table.to_csv("item_rating_table.csv", index=False)

# Display the final item rating table
print(item_rating_table)

# Count the number of "Like" and "Dislike" ratings
rating_counts = item_rating_table["rating_item"].value_counts()

# Display the counts
print("Rating Counts:")
print(rating_counts)


