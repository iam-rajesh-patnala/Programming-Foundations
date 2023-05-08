L = int(input())
count = 0
for i in range(1, L - 1):
    for j in range(i, L):
        for k in range(j + 1, L + 1):
            x = i * i
            y = j * j
            z = k * k
            if x + y == z:
                count = count + 1
print(count)
