import re

# Input text
text = input("Введіть рядок: ")

# Find all words
words = re.findall(r'\b[a-zA-Z0-9_-]+\b', text)

# Find the longest word
if words:
    longest = max(words, key=len)
    print("Найдовше слово:", longest)
else:
    print("Слів не знайдено.")