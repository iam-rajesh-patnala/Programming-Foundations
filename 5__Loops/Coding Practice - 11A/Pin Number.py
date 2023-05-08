word = input()

condition = True

for char in word:
    if char.isdigit():
        continue
    else:
        condition = False

print(condition)
