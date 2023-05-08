word = input().split()


first_letter =""
length_word = len(word)
count = 0

for i in word:
    count+= 1
    if count == length_word:
        length = len(i)
        first_letter += i[-length]
    else:
        length = len(i)
        first_letter += i[-length] + "."
    
print(first_letter)
