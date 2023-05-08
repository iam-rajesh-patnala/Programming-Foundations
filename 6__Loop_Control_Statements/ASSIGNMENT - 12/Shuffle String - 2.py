word1 = input()
word2 = input()

length = (len(word1))

new_string = ""

count = 0

for i in range(length):
    if i % 2 != 0:
        new_string += word2[i]
    else:
        new_string += word1[i]
print(new_string)