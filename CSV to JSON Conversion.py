import csv
import json

# Step 1: Read data from CSV file
csv_data = []

with open("input.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        csv_data.append(row)

# Step 2: Convert CSV data to JSON
json_data = json.dumps(csv_data, indent=4)

# Step 3: Write JSON data to output.json
with open("output.json", "w") as f:
    f.write(json_data)

print("CSV data has been converted to JSON and saved as output.json")

# Output:
# CSV data has been converted to JSON and saved as output.json