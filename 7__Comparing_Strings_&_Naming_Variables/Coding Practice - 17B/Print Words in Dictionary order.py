word = input()
first_word = "z"
last_word = "a"

new_word = ""

for i in range(len(word)):
    char = word[i]
    if char != " ":
        new_word += char
    if char == " " or i == (len(word)-1):
        if new_word.lower() < first_word.lower():
            first_word = new_word
        if new_word.lower() > last_word.lower():
            last_word = new_word
        new_word = ""
print(first_word, last_word)
        