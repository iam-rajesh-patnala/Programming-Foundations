word = input()

condition = True

for char in word:
    if char.islower():
        condition = False


print(condition)