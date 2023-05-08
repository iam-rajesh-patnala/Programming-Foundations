word = input()

result = ""

for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        result += char 

print(result)