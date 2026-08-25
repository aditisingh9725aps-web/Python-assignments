import re

text = input("Enter a text: ")

pattern = r'\w+@\w+\.\w+'

emails = re.findall(pattern, text)

if emails:
    print("Email addresses found:")
    for email in emails:
        print(email)
else:
    print("No email address found.")

"""
Email addresses found:
abc@gmail.com
xyz123@yahoo.com
"""