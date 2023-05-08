word = input().split()
length = len(word)
reverse_word = ""

for i in range(1, length + 1):
    reverse_word += word[-i] + " "
print(reverse_word)
