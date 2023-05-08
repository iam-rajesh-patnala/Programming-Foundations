word = input()
length = len(word)
masking = length - 4
masking = word[0:2] + "*" * masking + word[-2:]

print(masking)
