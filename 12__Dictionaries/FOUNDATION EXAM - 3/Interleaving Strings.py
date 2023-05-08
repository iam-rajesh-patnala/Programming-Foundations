word_1 = input()
word_2 = input()

length = min(len(word_1), len(word_2))

merged_word = ""

for i in range(length):
    merged_word+= word_1[i] + word_2[i]

if len(word_1) > length:
    merged_word+= word_1[length:]
else:
    merged_word+= word_2[length:]

print(merged_word)