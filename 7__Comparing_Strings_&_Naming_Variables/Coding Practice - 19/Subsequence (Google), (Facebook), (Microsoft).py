word1 = input()  # abcde

word2 = input()  # ace

count = 0
length_word2 = len(word2)
for char in word1:
    if char == word2[count]:
        count += 1
        if count == length_word2:
            break
if count == length_word2:
    print("Yes")
else:
    print("No")

# Yes
