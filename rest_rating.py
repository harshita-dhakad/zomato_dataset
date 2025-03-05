import pandas as pd
import numpy as np

# Load order data from CSV
orders_df = pd.read_csv("order.csv")

# Generating random ratings with 70% for 3, 4, 5 and 30% for 1, 2
orders_df["rating"] = np.random.choice([1, 2, 3, 4, 5], size=len(orders_df), p=[0.15, 0.15, 0.3, 0.3, 0.1])

# Selecting the required columns for the rating table
rating_table = orders_df[["orderId", "user_id", "date", "rating"]]

# Renaming columns to match the required format
rating_table.columns = ["order_id", "user_id", "date", "rating"]

# Save the rating table to a new CSV file
rating_table.to_csv("rating_table.csv", index=False)

# Display the final rating table
print(rating_table)