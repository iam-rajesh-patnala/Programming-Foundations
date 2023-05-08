word = input()
length = len(word)
masked = length -2
masked = word[0] +"*" * masked + word[length-1]

print(masked)
