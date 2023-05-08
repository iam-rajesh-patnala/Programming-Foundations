num = int(input())


sum = 0

for i in range(1, num + 1):
    length = len(str(i))
    sum = sum + length
print(sum)
