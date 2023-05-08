num = int(input())

count = 0

for i in range(1, num):
    for j in range(1, i + 1):
        res = i + j + 1
        if res == num:
            count += 1
print(count)
