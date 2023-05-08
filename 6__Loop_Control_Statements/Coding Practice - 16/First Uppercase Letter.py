word = input()

letter =""

for char in word:
    if char == char.isdigit():
        break
    if char == char.upper() and (not char.isdigit()):
        letter = char
        break
print(letter)