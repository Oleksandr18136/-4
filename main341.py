# Input two characters
char1 = input("Введіть перший символ: ")
char2 = input("Введіть другий символ: ")

# Get ASCII codes
start = ord(char1)
end = ord(char2)

# Get characters between them
result = "".join(chr(i) for i in range(start, end + 1))

# Print result
print("Результат:", result)