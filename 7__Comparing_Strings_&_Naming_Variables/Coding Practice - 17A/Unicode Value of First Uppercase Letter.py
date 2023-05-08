word = input()

for char in word:
    if char.isupper():
        print(ord(char))
        break