num = int(input())

count = 0

for i in range(1, num + 1):
    for j in range(i + 1, num + 1):
        for k in range(j + 1, num + 1):
            res = i + j + k
            if res == num:
                count += 1
print(count)
