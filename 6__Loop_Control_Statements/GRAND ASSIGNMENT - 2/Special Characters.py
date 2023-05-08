word = input()
count_vowels = 0
consonents = 0

for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        count_vowels += 1
    elif char == " ":
        pass
    else:
        consonents += 1

print(count_vowels)
print(consonents)
