word = input()

for char in word:
    if word[0] == "_" or word.isalpha():
        print(True)
        break
    else:
        print(False)
        break