word = input()

val = ""

for i in range(len(word)):
    index = int(input())
    val += word[index]

for char in val:
    print(char)