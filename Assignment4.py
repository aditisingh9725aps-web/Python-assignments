# Fibonacci Series using Dynamic Programming

# ---------------- Memoization (Top-Down) ----------------
def fib_memo(num, memory):
    if num <= 1:
        return num

    if memory[num] != -1:
        return memory[num]

    memory[num] = fib_memo(num - 1, memory) + fib_memo(num - 2, memory)
    return memory[num]


# ---------------- Tabulation (Bottom-Up) ----------------
def fib_tab(num):
    if num <= 1:
        return num

    table = [0] * (num + 1)
    table[0] = 0
    table[1] = 1

    for i in range(2, num + 1):
        table[i] = table[i - 1] + table[i - 2]

    return table[num]


# Main Program
num = int(input("Enter a number: "))

# Memoization Result
memory = [-1] * (num + 1)
result1 = fib_memo(num, memory)

# Tabulation Result
result2 = fib_tab(num)

print("\nResult using Memoization :", result1)
print("Result using Tabulation  :", result2)


# ---------------- SAMPLE OUTPUT ----------------
#
# Enter a number: 12
#
# Result using Memoization : 144
# Result using Tabulation  : 144