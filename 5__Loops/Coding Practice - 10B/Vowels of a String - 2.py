word = input()

count = 0

for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        count+= 1

if count > 2:
    print("String has more than two vowels")
else:
    print("String doesn't have more than two vowels")