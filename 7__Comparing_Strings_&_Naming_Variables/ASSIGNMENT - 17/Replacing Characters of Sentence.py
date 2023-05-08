word = input()

full_word = ""
for char in word:
    if char == " ":
        full_word += char
        continue
    order = ord(char)
    full_word = full_word + chr(order+1)
print(full_word)
        
        