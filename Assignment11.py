import pandas as pd
import numpy as np

# Create a Series containing 10 random numbers
s = pd.Series(np.random.randint(1, 100, 10))

print("Series:")
print(s)

# Indexing
print("\nElement at index 3:")
print(s[3])

# Filtering
print("\nNumbers greater than 50:")
print(s[s > 50])

# Statistical operations
print("\nMean:", s.mean())
print("Median:", s.median())
print("Minimum:", s.min())
print("Maximum:", s.max())

# Output:
# Series:
# 0    23
# 1    67
# 2    12
# 3    89
# 4    45
# 5    76
# 6    34
# 7    91
# 8    18
# 9    55
#
# Element at index 3:
# 89
#
# Numbers greater than 50:
# 1    67
# 3    89
# 5    76
# 7    91
# 9    55
#
# Mean: 51.0
# Median: 50.0
# Minimum: 12
# Maximum: 91