import argparse

# Create parser
parser = argparse.ArgumentParser(description="Mini Calculator CLI")

# Add positional arguments
parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")

# Add optional argument
parser.add_argument(
    "--operation",
    choices=["add", "sub", "mul", "div"],
    default="add",
    help="Operation to perform (default: add)"
)

# Parse arguments
args = parser.parse_args()

# Perform calculation
if args.operation == "add":
    result = args.num1 + args.num2

elif args.operation == "sub":
    result = args.num1 - args.num2

elif args.operation == "mul":
    result = args.num1 * args.num2

elif args.operation == "div":
    if args.num2 != 0:
        result = args.num1 / args.num2
    else:
        result = "Error: Division by zero"

# Print result
print(f"Result: {result}")

# Example command:
# python calculator_cli.py 10 5 --operation mul

# Output:
# Result: 50.0