word = input().split()

reversed_word = ""

for i in word:
    res = i[::-1]
    reversed_word += res + " "
print(reversed_word)
