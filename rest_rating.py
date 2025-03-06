import pandas as pd
import numpy as np

# Load order data from CSV
orders_df = pd.read_csv("order.csv")

# Get unique restaurant IDs
unique_restaurants = orders_df["restaurant_id"].unique()

# Ensure there are enough unique restaurants for selection
num_high = 20
num_upper_mid = 30
num_low = 50
num_rest = len(unique_restaurants) - (num_high + num_upper_mid + num_low)

# Randomly assign restaurants to categories
high_rated_restaurants = np.random.choice(unique_restaurants, size=num_high, replace=False)
remaining_restaurants = [r for r in unique_restaurants if r not in high_rated_restaurants]
upper_mid_rated_restaurants = np.random.choice(remaining_restaurants, size=num_upper_mid, replace=False)
remaining_restaurants = [r for r in remaining_restaurants if r not in upper_mid_rated_restaurants]
low_rated_restaurants = np.random.choice(remaining_restaurants, size=num_low, replace=False)
avg_rated_restaurants = [r for r in remaining_restaurants if r not in low_rated_restaurants]

# Function to assign ratings based on restaurant category
def assign_rating(restaurant_id):
    if restaurant_id in high_rated_restaurants:
        return np.random.choice([4, 5], p=[0.3, 0.7])  # More 5s than 4s for avg ~4.5-4.8
    elif restaurant_id in upper_mid_rated_restaurants:
        return np.random.choice([3, 4, 5], p=[0.2, 0.5, 0.3])  # Mostly 4s, some 5s & 3s
    elif restaurant_id in low_rated_restaurants:
        return np.random.choice([1, 2], p=[0.6, 0.4])  # Mostly 1s & 2s for avg ~1.5-2.5
    else:
        return np.random.choice([1, 2, 3, 4, 5], p=[0.15, 0.15, 0.3, 0.3, 0.1])  # Normal distribution

# Assign ratings to orders
orders_df["rating"] = orders_df["restaurant_id"].apply(assign_rating)

# Select required columns for rating table
rating_table = orders_df[["orderId", "user_id", "restaurant_id", "date", "rating"]]

# Rename columns to match required format
rating_table.columns = ["order_id", "user_id", "restaurant_id", "date", "rating"]

# Save the rating table to a new CSV file
rating_table.to_csv("rating_table.csv", index=False)

# Display the final rating table
print("Rating Table:")
print(rating_table.head())

# Aggregate ratings per restaurant
restaurant_ratings = rating_table.groupby("restaurant_id")["rating"].agg(["count", "mean"]).reset_index()
restaurant_ratings.columns = ["restaurant_id", "total_ratings", "average_rating"]

# Sort restaurants by average rating
restaurant_ratings = restaurant_ratings.sort_values(by="average_rating", ascending=False)

# Display aggregated restaurant ratings
print("\nAggregated Restaurant Ratings (Sorted by Average Rating Descending):")
print(restaurant_ratings)

# Check distribution summary
print("\nSummary Statistics of Restaurant Ratings:")
print(restaurant_ratings["average_rating"].describe())
