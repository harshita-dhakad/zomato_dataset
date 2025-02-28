import pandas as pd
import random

orderdf = pd.read_csv("./order_list.csv")


# Count distinct order_id values
distinct_count = orderdf['orderId'].nunique()

print(distinct_count)
