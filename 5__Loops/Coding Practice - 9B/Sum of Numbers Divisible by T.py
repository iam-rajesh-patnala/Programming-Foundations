T = int(input())
M = int(input())
N = int(input())

sum = 0
for i in range(M, N + 1):
    if (i % T) == 0:
        sum = sum + i
print(sum)
