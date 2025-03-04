import pandas as pd
import random

# Load the CSV data into a DataFrame
orderdf = pd.read_csv('./order_list.csv')

# Group by 'orderId' and aggregate the necessary columns
result = orderdf.groupby('orderId').agg(
    Total_price=('total_price', 'sum'),
    user_id=('user_id', 'first'),
    restaurant_id=('restaurantId', 'first'),
    date=('date', 'first')
)

# Define the list of payment methods
payment_methods = ["Cash", "UPI", "Card"]

# Generate a random payment method for each row in the DataFrame
random_payment_methods = [random.choice(payment_methods) for _ in range(len(result))]

# Add the 'new column' to the DataFrame
result.insert(1, "payment_method", random_payment_methods)

# Print the result
result.to_csv("order.csv", index=False)
