word_1 = input()
word_2 = input()

length_of_word_2 = len(word_2)

word_1 = word_1[:length_of_word_2]

if word_1 == word_2:
    print(True)
else:
    print(False)
