# ============================================================
# UNIT 2 - OPTION 1 & OPTION 2
# FIBONACCI SERIES USING DYNAMIC PROGRAMMING
# ============================================================


# ============================================================
# OPTION 1 - FIBONACCI USING MEMOIZATION
# TOP-DOWN DYNAMIC PROGRAMMING
# ============================================================

def fibonacci_memo(n, memo):
    if n <= 1:
        return n

    if n not in memo:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)

    return memo[n]


n = int(input("Enter the number of Fibonacci numbers: "))

memo = {}

print("Fibonacci Sequence using Memoization:")
for i in range(n):
    print(fibonacci_memo(i, memo), end=" ")


# ============================================================
# OPTION 1 - OUTPUT
# ============================================================

# Enter the number of Fibonacci numbers: 10
# Fibonacci Sequence using Memoization:
# 0 1 1 2 3 5 8 13 21 34


# ============================================================
# OPTION 2 - FIBONACCI USING TABULATION
# BOTTOM-UP DYNAMIC PROGRAMMING
# ============================================================

def fibonacci_tabulation(n):
    if n <= 0:
        return []

    dp = [0] * n

    if n > 1:
        dp[1] = 1

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp


n = int(input("Enter the number of Fibonacci numbers: "))

result = fibonacci_tabulation(n)

print("Fibonacci Sequence using Tabulation:")
print(*result)


# ============================================================
# OPTION 2 - OUTPUT
# ============================================================

# Enter the number of Fibonacci numbers: 10
# Fibonacci Sequence using Tabulation:
# 0 1 1 2 3 5 8 13 21 34