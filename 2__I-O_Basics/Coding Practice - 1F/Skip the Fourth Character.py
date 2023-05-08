word = input()
length = len(word)
total_word = ""

for i in range( length):
    if i == 3:
        pass
    else:
        total_word += word[i]
print(total_word)