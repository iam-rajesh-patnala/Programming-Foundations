def first_upper_case(char):
    return char.isupper()


word = input()

for char in word:
    if first_upper_case(char):
        print(char)
        break
