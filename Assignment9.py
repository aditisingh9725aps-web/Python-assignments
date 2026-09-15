import csv
import json

with open("data.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    
    data = list(csv_reader)


with open("output.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("CSV data successfully converted to JSON.")

# Output:
# CSV data successfully converted to JSON.

# Contents of output.json:
# [
#     {
#         "Name": "Alice",
#         "Age": "20",
#         "Course": "BTech"
#     },
#     {
#         "Name": "Bob",
#         "Age": "21",
#         "Course": "BCA"
#     },
#     {
#         "Name": "Charlie",
#         "Age": "19",
#         "Course": "BTech"
#     }
# ]