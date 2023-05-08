word = input()
num = int(input())
letter = input()


full_word = word[:num]
next_word = word[num + 1 :]

print(full_word + letter + next_word)
