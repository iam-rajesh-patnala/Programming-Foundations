word = input()

for char in word:
    if char.isdigit():
        print(ord(char))
        break