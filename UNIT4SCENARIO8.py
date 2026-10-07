import numpy as np
import pandas as pd

# Create a NumPy array of product prices
prices = np.array([50, 120, 80, 200, 150, 90])

# Calculate mean, median, maximum and minimum price
mean_price = np.mean(prices)
median_price = np.median(prices)
maximum_price = np.max(prices)
minimum_price = np.min(prices)

print("Mean Price:", mean_price)
print("Median Price:", median_price)
print("Maximum Price:", maximum_price)
print("Minimum Price:", minimum_price)

# Create a Pandas DataFrame
df = pd.DataFrame({
    "Item": ["Rice", "Sugar", "Oil", "Biscuits", "Milk", "Tea"],
    "Price": prices,
    "Quantity": [15, 8, 5, 20, 7, 12]
})

print("\nGrocery Inventory:")
print(df)

# Display grocery items having quantity less than 10
print("\nItems with quantity less than 10:")
print(df[df["Quantity"] < 10])


# OUTPUT:
# Mean Price: 115.0
# Median Price: 105.0
# Maximum Price: 200
# Minimum Price: 50
#
# Grocery Inventory:
#        Item  Price  Quantity
# 0      Rice     50        15
# 1     Sugar    120         8
# 2       Oil     80         5
# 3  Biscuits    200        20
# 4      Milk    150         7
# 5       Tea     90        12
#
# Items with quantity less than 10:
#     Item  Price  Quantity
# 1  Sugar    120         8
# 2    Oil     80         5
# 4   Milk    150         7