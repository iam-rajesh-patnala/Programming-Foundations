word = input()

upper = ""
for char in word:
    if char.isupper():
        upper += char

print(upper)