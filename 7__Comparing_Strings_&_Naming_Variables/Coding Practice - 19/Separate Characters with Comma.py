word = input()

# list_a = []

# for char in word:
#     list_a.append(char)

# print(*list_a, sep = ",")

new = ""
for i in range(len(word)):
    if i < len(word)-1:
        new += word[i] + ","
    else:
        new += word[i]

print(new)