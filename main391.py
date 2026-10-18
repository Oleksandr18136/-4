import re

# Input text
text = input("Введіть рядок з числами та словами: ")

# Find all numbers
numbers = re.findall(r'\d+', text)

# Join with commas
result = ", ".join(numbers)

# Print result
print("Результат:", result)