L = ["5", "eat", "9.80", "Water", "python", "-678", "7685.26", "-2.5", "sing"]

# Write your code here

word = input() # Water

# bigener way

# for char in L:
#     if char == word:
#         print(True)
#         break
#     else:
#         print(False)


if word in L:
    print(True)
else:
    print(False)

# true