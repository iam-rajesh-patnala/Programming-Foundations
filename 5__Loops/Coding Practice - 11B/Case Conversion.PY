word = input()


modified_word = word[0]


for char in word[1:]:
    if char.isupper():
        modified_word += " " + char
    else:
        modified_word += char

print(modified_word)
