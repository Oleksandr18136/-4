# Input text
text = input("Введіть рядок: ")

# Find middle index
mid = (len(text) + 1) // 2

# Swap two halves
part1 = text[:mid]
part2 = text[mid:]
result = part2 + part1

# Print result
print("Результат:", result)