import numpy as np
import pandas as pd

# Create a NumPy array of electricity bills
bills = np.array([2500, 3200, 1800, 4500, 2900, 3700])

# Calculate mean, median, maximum and minimum
mean_bill = np.mean(bills)
median_bill = np.median(bills)
maximum_bill = np.max(bills)
minimum_bill = np.min(bills)

print("Mean Bill:", mean_bill)
print("Median Bill:", median_bill)
print("Maximum Bill:", maximum_bill)
print("Minimum Bill:", minimum_bill)

# Create a Pandas DataFrame
df = pd.DataFrame({
    "Consumer": ["A", "B", "C", "D", "E", "F"],
    "Bill Amount": bills
})

print("\nElectricity Bill Data:")
print(df)

# Display consumers whose bill exceeds ₹3000
print("\nConsumers with bill exceeding ₹3000:")
print(df[df["Bill Amount"] > 3000])


# OUTPUT:
# Mean Bill: 3100.0
# Median Bill: 3050.0
# Maximum Bill: 4500
# Minimum Bill: 1800
#
# Electricity Bill Data:
#   Consumer  Bill Amount
# 0        A         2500
# 1        B         3200
# 2        C         1800
# 3        D         4500
# 4        E         2900
# 5        F         3700
#
# Consumers with bill exceeding ₹3000:
#   Consumer  Bill Amount
# 1        B         3200
# 3        D         4500
# 5        F         3700