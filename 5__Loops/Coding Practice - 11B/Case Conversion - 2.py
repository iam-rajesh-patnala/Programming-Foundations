word = input()

modified_word = ""


for char in word:
    if char.isupper():
        modified_word += "-" + char.lower()
    else:
        modified_word += char

print(modified_word)