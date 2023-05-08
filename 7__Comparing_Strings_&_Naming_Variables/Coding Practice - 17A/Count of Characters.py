word = input()

num = int(input())

count = 0
for char in word:
    if ord(char) == num:
        count += 1

print(count)