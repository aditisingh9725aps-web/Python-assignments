 # file_processor.py

input_file = "input.txt"
output_file = "output.txt"

# Open the input file and read all lines
with open(input_file, "r") as file:
    lines = file.readlines()

# Count the number of lines
line_count = len(lines)

# Extract the first two lines
first_two_lines = lines[:2]

# Write the extracted lines to a new file
with open(output_file, "w") as file:
    file.writelines(first_two_lines)

# Display the results
print("Total number of lines:", line_count)
print("First two lines have been written to", output_file)

"""  
Output
Hello World
Python Programming

"""