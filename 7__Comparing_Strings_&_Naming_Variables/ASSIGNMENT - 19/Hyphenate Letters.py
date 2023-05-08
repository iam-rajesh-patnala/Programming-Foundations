word = input()

length = len(word)
full_word = ""
count = 0

for char in word:
    if char==" ": #remove spaces from total word
      continue
    elif count == 0: #except first word is hyphen is not applicable
        full_word += char
        count+= 1
    elif count < length:
        hyphen = '-'+char
        full_word+= hyphen
        count+= 1
print(full_word)