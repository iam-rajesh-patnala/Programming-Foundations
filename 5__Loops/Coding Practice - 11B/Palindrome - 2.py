word = input()
reverse_word = ""
for i in word:
    reverse_word = i + reverse_word
if (reverse_word.lower()) == (word.lower()):
    print("True")
else:
    print("False")
