word = input()

starter = word

check = ""

for i in range(len(word)):
    check += word[i]

    if word[i] == " " or i == word[len(word) - 1]:
        if check.lower() < starter.lower():
            starter = check
        check = ""
print(starter)