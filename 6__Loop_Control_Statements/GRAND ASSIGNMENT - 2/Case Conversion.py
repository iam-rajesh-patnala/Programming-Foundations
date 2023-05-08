word = input()

count = 0
pin = ""

for char in word:
    if char == char.upper():
        count += 1
        if not count <= 1:
            char = "_" + char
        char = char.lower()
    pin = pin+char
print(pin)
