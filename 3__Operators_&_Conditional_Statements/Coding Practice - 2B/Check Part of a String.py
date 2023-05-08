word_1 = input()
word_2 = input()
num = int(input())

length =len(word_2)
part = word_1[num:]
part = part[:length]

if part == word_2:
    print(True)
else:
    print(False)