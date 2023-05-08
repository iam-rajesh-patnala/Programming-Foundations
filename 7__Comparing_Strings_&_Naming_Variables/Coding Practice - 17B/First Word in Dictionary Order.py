word = input()

first_word = word
status = ""

for i in range(len(word)):
    char = word[i]
    status += char

    if char == " " or i == len(word) - 1:
        if status.lower() < first_word.lower():
            first_word = status
        status = ""
print(first_word)
