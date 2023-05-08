num = input().split()
length = len(num)
total = 0

for i in range(length):
    total += int(num[i])
print(total)
