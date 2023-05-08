word = input()
total = ""
for char in word:
    if char.isdigit():
        total = total + char
print(total)
