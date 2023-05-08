word = input()  # Five

first = word[0]
last = ""


for i in range(1, len(word) - 1):
    if ord(word[i]) > ord(first):
        last = word[i]

    else:
        first = word[i]

print(first, last)  # F  V
