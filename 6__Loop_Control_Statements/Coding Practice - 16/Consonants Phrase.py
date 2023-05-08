word = input()
vowels = set(["a", "e", "i", "o", "u"]) # using a set for faster lookup

result = "".join(letter for letter in word if letter not in vowels) # using a generator expression and join method

print(result)
