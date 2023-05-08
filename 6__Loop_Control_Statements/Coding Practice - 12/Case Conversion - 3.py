word = input()


result = word[0].lower()

for char in word[1:]:
    if char.isupper():
        result += "-" + char.lower()
    else:
        result += char

print(result)
    
