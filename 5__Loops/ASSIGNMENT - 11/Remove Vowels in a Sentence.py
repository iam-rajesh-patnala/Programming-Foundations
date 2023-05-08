word = input()
vowels = ("a", "e", "i", "o", "u")

for letter in word:
    if letter.lower() in vowels:
        word = word.replace(letter, "")
print(word)
