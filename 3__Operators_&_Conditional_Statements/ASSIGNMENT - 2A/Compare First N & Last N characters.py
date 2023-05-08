word = input()
num = int(input())

first_word = word[:num]
second_word = word[-num:]

if first_word == second_word:
    print(False)
else:
    print(True)