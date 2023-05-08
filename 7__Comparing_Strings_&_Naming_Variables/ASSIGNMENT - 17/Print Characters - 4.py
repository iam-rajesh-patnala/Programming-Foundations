word = input()

num1 = int(input())
num2 = int(input())

new = ""

for char in word:
    for i in range(num1, num2 + 1):
        if ord(char) == i:
            new += char + " "
print(new)
