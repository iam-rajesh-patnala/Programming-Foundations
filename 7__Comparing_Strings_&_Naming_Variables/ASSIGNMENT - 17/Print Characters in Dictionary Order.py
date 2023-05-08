word = input()

first = word[0]
last = word[0]


for i in range(1, len(word) - 1):
    if ord(word[i]) > ord(first):
        first = word[i]
    elif ord(word[i]) < ord(last):
        last = word[i]

print(last, first)
