word = input()

for char in word:
    if word[0] == "_" or word[0].isalpha():
        print(True)
        break
    else:
        print(False)
        break