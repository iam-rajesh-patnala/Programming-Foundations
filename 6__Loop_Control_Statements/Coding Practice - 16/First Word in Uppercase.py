sentence = input()
count = 0

for char in sentence:
    if char == " ":
        break
    count += 1

first_word = sentence[:count]
cap = first_word.upper()
rem_word = sentence[count:]
print(cap+rem_word)
