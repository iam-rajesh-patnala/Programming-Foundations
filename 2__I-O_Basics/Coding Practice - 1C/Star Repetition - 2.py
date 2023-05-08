# word = input()
# length_of_word = len(word)
# total_word = ""
# count = 0

# for i in range(1, length_of_word+1):
#     if i == 1:
#         total_word+= word[count]
#         count+= 1
#     else:
#         total_word += word[count].replace(word[count], "*")
# print(total_word)


# word = input()

# length = len(word)

# total = ""
# for i in range(length):
#     if i == 0:
#         total+= word[i]
#     else:
#         total+= "*"
# print(total)


word = input()
length = len(word) - 1
first_word = word[0]
star = "*" * length

print(first_word + star)
