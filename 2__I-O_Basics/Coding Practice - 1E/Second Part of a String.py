word = input()
total = ""
for char in word:
    if char.isdigit():
        total += char
print(total)
