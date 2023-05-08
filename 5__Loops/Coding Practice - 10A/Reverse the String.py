word = input()
length = len(word)

# value = -1
reverse = ""
for i in range(1, length + 1):
    reverse = reverse + (word[-i])
    # value = value +(-1)
print(reverse)
