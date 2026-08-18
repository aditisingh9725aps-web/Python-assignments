# Assignment 3 – Regular Expressions

import re

# --------------------------------------------------
# Task 1: Count Words Starting with Capital Letters
# --------------------------------------------------

text1 = "Python is Great. Regex is Powerful."

result = re.findall(r"\b[A-Z]\w+", text1)

print("Task 1 Output:", result)

# Output:
# Task 1 Output: ['Python', 'Great', 'Regex', 'Powerful']


# --------------------------------------------------
# Task 2: Extract All Email Addresses
# --------------------------------------------------

text2 = "Contact us at support@example.com or admin@test.org"

pattern = r"[\w\.-]+@[\w\.-]+\.\w+"

emails = re.findall(pattern, text2)

print("Task 2 Output:", emails)

# Output:
# Task 2 Output: ['support@example.com', 'admin@test.org']


# --------------------------------------------------
# Task 3: Mask Sensitive Numbers
# --------------------------------------------------

text3 = "My card number is 1234-5678-9876-5432"

masked = re.sub(
    r"(\d{4})-(\d{4})-(\d{4})-(\d{4})",
    r"****-****-****-\4",
    text3
)

print("Task 3 Output:", masked)

# Output:
# Task 3 Output: My card number is ****-****-****-5432


# --------------------------------------------------
# Task 4: Extract Hashtags from a Tweet
# --------------------------------------------------

text4 = "Learning #Python #Regex #AI is fun!"

hashtags = re.findall(r"#\w+", text4)

print("Task 4 Output:", hashtags)

# Output:
# Task 4 Output: ['#Python', '#Regex', '#AI']


# --------------------------------------------------
# Task 5: Validate Phone Number Format
# --------------------------------------------------

phone = "123-456-7890"

if re.match(r"^\d{3}-\d{3}-\d{4}$", phone):
    print("Task 5 Output: Valid phone number")
else:
    print("Task 5 Output: Invalid phone number")

# Output:
# Task 5 Output: Valid phone number